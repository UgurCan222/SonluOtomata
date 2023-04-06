def contains_cadab(kelime):
    # Sonlu otomatın durumları tanımlanıyor
    durumlar = [0, 1, 2, 3, 4]
    
    # Sonlu otomatın geçişleri tanımlanıyor
    gecisler = {
        (0, 'c'): 1,
        (1, 'a'): 2,
        (2, 'd'): 3,
        (3, 'a'): 4,
        (4, 'b'): 4
    }
    
    # Sonlu otomatın kabul eden durumu tanımlanıyor
    kabul_durumu = 4
    
    # Geçerli durumu başlangıç durumu (0) olarak başlat
    gecerli_durum = 0
    # Geçerli durumun indeksi
    gecerli_index = 0
    # Sonlu otomatın kabul durumunun son indeksi
    kabul_index = None
    
    # Girdi kelimesindeki her karakter için döngü oluştur
    for harf in kelime:
        gecerli_index += 1
        # Geçerli karakterle geçerli durumdan bir geçişin olup olmadığını kontrol et
        if (gecerli_durum, harf) in gecisler:
            gecerli_durum = gecisler[(gecerli_durum, harf)]
        else:
            gecerli_durum = 0
            gecerli_index = 0
        
        # Geçerli durumun kabul durumu olup olmadığını kontrol et
        if gecerli_durum == kabul_durumu:
            kabul_index = gecerli_index - 1
    
    # Eğer alt dizi bulunursa, kabul indeksini ve alt dizginin konumunu yazdır
    if kabul_index is not None:
        print(f"'{kelime}' kelimesi 'cadab' alt kelimesini içerir, başlangıç indeksi: {kabul_index - 2}")
    else:
        print(f"'{kelime}' kelimesi 'cadab' alt kelimesini içermez.")

kelime = "abcadabadccdbabd"
contains_cadab(kelime)
