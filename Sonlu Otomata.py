def SonluOtomata(text):
    # Durum geçiş tablosu (states) tanımlanır.
    states = {
        (0, "c"): 1,
        (1, "a"): 2,
        (2, "d"): 3,
        (3, "a"): 4,
        (4, "b"): 4,
    }

    # Başlangıç kapısı (state_index) 0 olarak atanır.
    state_index = 0

    # Geçerli kapı (valid_index) 4 olarak atanır.
    valid_index = 4

    # Sonuç (result) None olarak atanır.
    result = None

    # Kelime sayısı (index_count) 0 olarak atanır.
    index_count = 0

    # Metindeki her kelime için bir döngü oluşturulur.
    for word in text:
        # Eğer kapılar sözlüğünde (states) mevcutsa, kapı indeksi güncellenir.
        if (state_index, word) in states:
            state_index = states[(state_index, word)]
        else:
            state_index = 0

        # Eğer geçerli kapı (valid_index) ulaşılmışsa, sonuç indeksi (index_count) güncellenir.
        if state_index == valid_index:
            result = index_count - 4

        # Eğer kelime, önceki kelimeye eşitse ve önceki kelime "c" ise, kapı indeksi güncellenir.
        if word == text[index_count - 1] and text[index_count - 1] == "c":
            state_index = 1

        # Kelime sayısı (index_count) artırılır.
        index_count += 1

    # Sonuç (result) değeri None değilse, cadab kelimesi metinde bulunmuştur.
    if result is not None:
        print(f"'{text}' metninde cadab kelimesi bu indekste bulundu: {result}")
    else:
        print(f"'{text}' metninde cadab kelimesi bulunamadı.")


# Örnek metin tanımlanır.
text = "abcasgbadccadabd"

# Sonlu Otomata eşleme fonksiyonu çağrılır.
SonluOtomata(text)
