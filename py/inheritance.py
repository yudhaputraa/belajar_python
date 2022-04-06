class Ojek():

    def __init__(self,nama,transmisi,daerah):
        self.nama = nama
        self.transmisi =transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama :',self.nama,'\nmotor :',self.transmisi,'\ndaerah :',self.daerah)

# di bawah ini yg dinamakan inheritance
class Gojek(Ojek):
    def cek_id_abang(self):
        print('cek aplikasi gojek')

ojek1 = Ojek('mario','manual','bandung selatan')
ojek2 = Gojek('bambang','automatic','sidoarjo')

ojek1.cek_id_abang()
ojek2.cek_id_abang()
