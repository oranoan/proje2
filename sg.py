import http.client
import json

# API anahtarınızı burada doğrudan tanımlayın
api_key = "3MQJiZ2n2iC3HI2MUHCqS7:2zdRo5GhQ5PCS5xhAju6A3"

# Kullanıcıya balkonunda çiçek yetiştirip yetiştirmediğini soruyoruz
cevap = input("Balkonunda çiçek yetiştiriyor musun? (evet/hayır): ").strip().lower()

# Hava durumu verilerini çekme işlemi
conn = http.client.HTTPSConnection("api.collectapi.com")
headers = {
    'content-type': "application/json",
    'authorization': f"apikey {api_key}"
}
conn.request("GET", "/weather/getWeather?data.lang=tr&data.city=ankara", headers=headers)

res = conn.getresponse()
data = res.read()

# Yanıtı JSON olarak çözümleme
weather_data = json.loads(data.decode("utf-8"))

# "Evet" cevabı alındıysa hangi bitkileri yetiştirdiğini sor
if cevap == "evet":
    bitki = input("Hangi bitkileri yetiştiriyorsunuz?: ").strip().lower()

    # Kullanıcı "aloe vera" yetiştiriyorsa bakım talimatları ve sulama tavsiyesi ver
    if bitki == "aloe vera":
        print(
            "\nAloe vera yetiştirmesi oldukça kolay olan bir bitkidir ve özellikle evde bakımı için çok uygundur. İşte aloe vera yetiştirme hakkında bilmeniz gereken temel adımlar:\n")
        print(
            "1. Toprak Seçimi:\nAloe vera, iyi drene olan ve su tutmayan bir toprakta yetişir. Kaktüs ve sukulentler için özel toprak karışımlarını tercih edebilirsiniz.")
        print("2. Saksı Seçimi:\nDrenaj delikleri olan bir saksı kullanın. Aloe veralar fazla suya duyarlıdır.")
        print("3. Işık İhtiyacı:\nAloe vera güneşi sever, ancak doğrudan güneş ışığı almamaya özen gösterin.")
        print(
            "4. Sulama:\nAloe vera suya dayanıklı bir bitkidir; fazla sulama çürümeye yol açabilir. Toprağın tamamen kurumasını bekleyin.")
        print("5. Sıcaklık ve Nem:\n15-25°C sıcaklık aralığında en iyi şekilde büyür, düşük nemi tolere eder.")
        print("6. Gübreleme:\nAloe veraya yılda bir veya iki kez hafif bir gübreleme yapılabilir.")
        print(
            "7. Çoğaltma:\nAloe vera, kök sürgünü adı verilen yavrular üreterek çoğalır. Bu yavruları ayırarak çoğaltabilirsiniz.\n")

        # Aloe vera için hava durumu verilerini kontrol et
        if 'result' in weather_data:
            for day_weather in weather_data['result']:
                tarih = day_weather.get('date')
                derece = day_weather.get('degree')
                max_derece = day_weather.get('max')
                min_derece = day_weather.get('min')
                durum = day_weather.get('description')
                nem = day_weather.get('humidity')
                ruzgar = day_weather.get('wind')

                # Günlük hava durumu bilgilerini yazdırma
                print(f"Tarih: {tarih}")
                print(f"Durum: {durum}")
                print(f"Şu Anki Sıcaklık: {derece}°C")
                print(f"En Yüksek Sıcaklık: {max_derece}°C")
                print(f"En Düşük Sıcaklık: {min_derece}°C")
                print(f"Nem Oranı: %{nem}")
                print(f"Rüzgar Hızı: {ruzgar} km/sa")

                # Yağmur kontrolü ve sulama kararı
                if "yağmur" in durum.lower():
                    print("Öneri: Bugün yağmur yağacak, balkondaki aloe verayı sulama.\n")
                else:
                    print("Öneri: Bugün yağmur yağmayacak, balkondaki aloe verayı sula.\n")
        else:
            print("Hava durumu verisi bulunamadı.")

    else:
        # Aloe vera dışındaki bitkiler için sulama tavsiyeleriyle birlikte haftalık hava durumu göster
        if 'result' in weather_data:
            for day_weather in weather_data['result']:
                tarih = day_weather.get('date')
                derece = day_weather.get('degree')
                max_derece = day_weather.get('max')
                min_derece = day_weather.get('min')
                durum = day_weather.get('description')
                nem = day_weather.get('humidity')
                ruzgar = day_weather.get('wind')

                # Günlük hava durumu bilgilerini yazdırma
                print(f"Tarih: {tarih}")
                print(f"Durum: {durum}")
                print(f"Şu Anki Sıcaklık: {derece}°C")
                print(f"En Yüksek Sıcaklık: {max_derece}°C")
                print(f"En Düşük Sıcaklık: {min_derece}°C")
                print(f"Nem Oranı: %{nem}")
                print(f"Rüzgar Hızı: {ruzgar} km/sa")

                # Yağmur kontrolü ve sulama kararı
                if "yağmur" in durum.lower():
                    print("Öneri: Bugün yağmur yağacak, balkondaki bitkileri sulama.\n")
                else:
                    print("Öneri: Bugün yağmur yağmayacak, balkondaki bitkileri sula.\n")
        else:
            print("Hava durumu verisi bulunamadı.")
else:
    # "Hayır" cevabı alındıysa sadece haftalık hava durumu ver
    if 'result' in weather_data:
        print("Haftalık Hava Durumu:")
        for day_weather in weather_data['result']:
            tarih = day_weather.get('date')
            derece = day_weather.get('degree')
            max_derece = day_weather.get('max')
            min_derece = day_weather.get('min')
            durum = day_weather.get('description')

            # Günlük hava durumu bilgilerini yazdırma
            print(f"Tarih: {tarih}")
            print(f"Durum: {durum}")
            print(f"Şu Anki Sıcaklık: {derece}°C")
            print(f"En Yüksek Sıcaklık: {max_derece}°C")
            print(f"En Düşük Sıcaklık: {min_derece}°C\n")
    else:
        print("Hava durumu verisi bulunamadı.")

conn.close()
