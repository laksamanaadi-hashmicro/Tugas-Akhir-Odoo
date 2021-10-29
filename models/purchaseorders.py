from odoo import models, fields, api

class Purchase(models.Model):
    _name = 'lec.purchase'
    _description = 'Daftar Orderan Pembelian'

    penjual_id = fields.Many2one (comodel_name='res.partner',
                                    string='Nama Penjual',
                                    domain="[('is_supplier','ilike',True)]",
                                    delegate=True)

    tanggal_pesan = fields.Datetime(string='Tanggal Pemesanan', default=fields.Datetime.now)

    jenis_pembayaran = fields.Selection(
        string='Jenis Pembayaran',
        selection=[
                    ('pay later', 'Pay Later'),
                    ('transfer bank', 'Transfer Bank'),
                    ('cash on delivery', 'Cash on Delivery')
                ]
        )

    note = fields.Char(string='Note', help='isi dengan pesan tambahan jika perlu')
    
    detail_jpo_ids = fields.One2many(comodel_name='lec.detailpo', inverse_name='po_id',string='Detail Orderan Penjualan')

    jumlah_po = fields.Char(compute='_compute_jumlah_po', string='Jumlah Pesanan')

    @api.depends('detail_jpo_ids')
    def _compute_jumlah_po(self):        
        for record in self:
            record.jumlah_po +=len(record.detail_jpo_ids)

    total_harga_po = fields.Integer(compute='_compute_total_harga_po', string='Total Tagihan')
    
    @api.model
    def _compute_total_harga_po(self):
        for rec in self:
            total = sum(self.env['lec.detailpo'].search([('po_id','=',rec.id)]).mapped('jumlah_harga_po'))
            rec.total_harga_po = total

class DetailPO(models.Model):
    _name = 'lec.detailpo'
    _description = 'Detail Orderan Penjualan'

    name = fields.Char(string='Kode Order Penjualan')

    po_id = fields.Many2one(comodel_name='lec.purchase', string='Kode Order Penjualan')

    nama_barang = fields.Many2one(comodel_name='product.template', string='Nama Barang')
    
    harga_po = fields.Integer(
        compute='_compute_harga_po', 
        string='Harga Barang')

    @api.depends('nama_barang')
    def _compute_harga_po(self):
        for record in self:
            record.harga_po = record.nama_barang.list_price

    jumlah_barang_po = fields.Integer(
        string='Jumlah Barang')
    
    jumlah_harga_po = fields.Integer(
        compute='_compute_field_jhpo', 
        string='Jumlah Harga')

    @api.depends('jumlah_barang_po')
    def _compute_field_jhpo(self):
        for record in self:
            record.jumlah_harga_po = record.jumlah_barang_po * record.harga_po