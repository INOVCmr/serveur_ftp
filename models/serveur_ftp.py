from odoo import models, fields, api
from odoo.exceptions import UserError
import os
import ftplib

class ServeurFtp(models.Model):
    _name = 'serveur.ftp'
    _description = 'Configuration FTP'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Nom du fichier", required=True)
    ftp_address = fields.Char("Adresse FTP", required=True)
    ftp_user = fields.Char("Nom d'utilisateur FTP", required=True)
    ftp_password = fields.Char("Mot de passe FTP", required=True)
    local_path = fields.Char("Chemin local du fichier", required=True)
    destinataire_email = fields.Char("Destinataire de l'email")
    interval_number = fields.Integer("Nombre d'intervalles", default=1)
    interval_type = fields.Selection([
        ('minutes', 'Minutes'),
        ('hours', 'Heures'),
        ('days', 'Jours')
    ], string="Type d'intervalle", default='days')
    cron_id = fields.Many2one('ir.cron', string="Tâche planifiée liée", ondelete='set null')
    upload_status = fields.Selection([
        ('pending', 'En attente'),
        ('success', 'Succès'),
        ('failed', 'Échec')
    ], string="Statut d'upload", default='pending')

    def action_envoyer(self):
        """Bouton manuel qui envoie le fichier et crée un cron associé"""
        for record in self:
            record.envoyer_fichier()
            record._create_or_update_cron()

    def envoyer_fichier(self):
        """Méthode d'envoi FTP"""
        for record in self:
            file_path = record.local_path
            if not os.path.isfile(file_path):
                raise UserError(f"Le fichier n'existe pas : {file_path}")

            try:
                with ftplib.FTP(record.ftp_address) as ftp:
                    ftp.login(record.ftp_user, record.ftp_password)
                    with open(file_path, 'rb') as f:
                        ftp.storbinary(f'STOR {record.name}', f)
                record.upload_status = 'success'
            except Exception as e:
                record.upload_status = 'failed'
                raise UserError(f"Erreur FTP : {str(e)}")
        
        # 2. Envoi de l'email
        sujet = "Fichier envoyé avec succès"
        corps = f"Bonjour,\n\nLe fichier '{self.name}' a bien été envoyé sur le serveur FTP '{self.ftp_address}'.\n\nCordialement !!!!,\nOdoo"

        if not self.destinataire_email:
            raise UserError("Aucune adresse email renseignée pour l'envoi.")

        self.env['mail.mail'].create({
            'subject': sujet,
            'body_html': f'<p>{corps}</p>',
            'email_to': self.destinataire_email,
        }).send()

        # (Optionnel) Ajouter un message dans le fil de discussion
        self.message_post(body="Le fichier a été envoyé par FTP et l'email de confirmation a été expédié.")


    @api.model
    def create(self, vals):
        record = super().create(vals)
        return record

    def write(self, vals):
        result = super().write(vals)
        return result

    def _create_or_update_cron(self):
        for rec in self:
            cron_name = f'cron_envoi_ftp_{rec.id}'
            existing_cron = self.env['ir.cron'].search([('name', '=', cron_name)], limit=1)

            model_ref = self.env['ir.model'].search([('model', '=', 'serveur.ftp')], limit=1)

            if not model_ref:
                raise UserError("Référence au modèle 'serveur.ftp' introuvable.")

            cron_vals = {
                'name': cron_name,
                'model_id': model_ref.id,
                'state': 'code',
                'code': f"model.browse({rec.id}).envoyer_fichier()",
                'interval_number': rec.interval_number,
                'interval_type': rec.interval_type,
                'numbercall': -1,
                'doall': False,
            }

            if existing_cron:
                existing_cron.write(cron_vals)
                rec.cron_id = existing_cron
            else:
                new_cron = self.env['ir.cron'].create(cron_vals)
                rec.cron_id = new_cron

    @api.model
    def setup_cron_task(self, cr, registry):
        """Fallback global (au cas où) pour recréer tous les crons manquants"""
        env = api.Environment(cr, 1, {})
        for rec in env['serveur.ftp'].search([]):
            rec._create_or_update_cron()
