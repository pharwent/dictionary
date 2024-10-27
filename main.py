meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "LMAO": "Tanggapan lebih ekstrim kepada hal yang lucu"
            }
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!):")
    if word in meme_dict.keys():
        print(word,"berarti",meme_dict[word])
    else:
        print("huh? apa? gak ada kata itu.")
