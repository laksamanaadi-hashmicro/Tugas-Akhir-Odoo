from odoo import models, fields, api

class Sales(models.Model):
    _name = 'lec.sales'
    _description = 'Daftar Orderan Penjualan'

    pembeli_id = fields.Many2one (comodel_name='res.partner',
                                    string='Nama Pembeli',
                                    domain="[('is_customer','ilike',True)]",
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
    
    tanggal_kirim = fields.Datetime(string='Tanggal Pengiriman', default=fields.Datetime.now)

    note = fields.Char(string='Note', help='isi dengan pesan tambahan jika perlu')
    
    detail_jso_ids = fields.One2many(comodel_name='lec.detailso', inverse_name='so_id',string='Detail Orderan Penjualan')

    jumlah_so = fields.Char(compute='_compute_jumlah_so', string='Jumlah Pesanan')

    @api.depends('detail_jso_ids')
    def _compute_jumlah_so(self):        
        for record in self:
            record.jumlah_so +=len(record.detail_jso_ids)

    total_harga_so = fields.Integer(compute='_compute_total_harga_so', string='Total Tagihan')
    
    @api.model
    def _compute_total_harga_so(self):
        for rec in self:
            total = sum(self.env['lec.detailso'].search([('so_id','=',rec.id)]).mapped('jumlah_harga_so'))
            rec.total_harga_so = total

class DetailSO(models.Model):
    _name = 'lec.detailso'
    _description = 'Detail Orderan Penjualan'

    name = fields.Char(string='Kode Order Penjualan')

    so_id = fields.Many2one(comodel_name='lec.sales', string='Kode Order Penjualan')

    nama_barang = fields.Many2one(comodel_name='product.template', string='Nama Barang')
    
    harga_so = fields.Integer(
        compute='_compute_harga_so', 
        string='Harga Barang')

    @api.depends('nama_barang')
    def _compute_harga_so(self):
        for record in self:
            record.harga_so = record.nama_barang.list_price

    jumlah_barang_so = fields.Integer(
        string='Jumlah Barang')
    
    jumlah_harga_so = fields.Integer(
        compute='_compute_field_jhso', 
        string='Jumlah Harga')

    @api.depends('jumlah_barang_so')
    def _compute_field_jhso(self):
        for record in self:
            record.jumlah_harga_so = record.jumlah_barang_so * record.harga_so

    