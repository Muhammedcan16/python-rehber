rehber = {

    'kişi1' :{
      'cep':'0599854',
      'iş':'0599854545',
      'ev':'059985454532'
    } ,
    'kişi2' :{
      'cep':'0599854',
      'iş':'0599854545',
      'ev':'059985454532'
    },
    'kişi3' :{
      'cep':'0599854',
      'iş':'0599854545',
      'ev':'059985454532'
    }


}

isimler = rehber.keys()#ilk verilerim
kisi = input('numarasını görmek istediğiniz kişiyi giriniz:')
no = input('{} Kişinin hangi numarasını istiyorsunuz: '.format(kisi))
if kisi in isimler :
  Flag = True
else:
  Flag = False

if Flag == True :
  print(rehber.get(kisi,'Kişi bulunamadı').get(no,'{} numarası mevcut değil'.format(no)))
else:
  print('Lütfen rehbere kayıtlı bir kişi girin!')



