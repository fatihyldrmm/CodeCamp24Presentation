# 1. Gün - Introduction to DevOps

Staj programımızın ilk gününde DevOps'un temel kavramları ve metodolojileri hakkında bilgi edindik. DevOps, yazılım geliştirme (Development) ve operasyon (Operations) ekiplerini bir araya getirerek daha hızlı, daha güvenilir ve sürekli teslimat sağlayan bir kültür, yöntem ve araçlar topluluğudur.

## DevOps Nedir?
- **DevOps**: Yazılım geliştirme ve IT operasyonları arasındaki iletişimi, iş birliğini ve entegrasyonu artırarak, yazılım ve hizmetlerin yüksek hızda teslim edilmesini sağlayan bir felsefe ve uygulama bütünüdür. DevOps, yazılım geliştirme yaşam döngüsünün her aşamasında (planlama, geliştirme, test etme, dağıtma, izleme ve bakım) hız, verimlilik ve güvenlik sağlar.

## DevOps Metodolojisi
- **Amaç**: Sistem geliştirme yaşam döngüsünü kısaltmak ve yüksek kaliteli yazılımların sürekli teslimatını sağlamak.
- **Temel İlkeler**:
  - **Automation**: Yazılım geliştirme yaşam döngüsünün otomasyonu.
  - **Collaboration and communication**: Ekipler arası sürekli iş birliği ve iletişim.
  - **Continuous improvement and minimization of waste**: Sürekli iyileştirme süreçleri ve verimsizliklerin ortadan kaldırılması.
  - **Hyperfocus on user needs with short feedback loops**: Kısa geri bildirim döngüleri ile kullanıcı ihtiyaçlarının ön planda tutulması.

## DevOps Kültürünün Faydaları
- **Hız**: Yazılım geliştirme ve dağıtım süreçlerini hızlandırarak, müşteri ihtiyaçlarına daha hızlı yanıt verme.
- **Sürekli Teslimat**: Yazılım güncellemelerinin daha sık ve düzenli olarak yapılmasını sağlama.
- **Güvenilirlik**: Uygulama güncellemelerinin ve altyapı değişikliklerinin güvenilir bir şekilde teslim edilmesini sağlama.
- **Ölçeklenebilirlik**: Altyapı ve geliştirme süreçlerini ölçeklenebilir hale getirme.
- **Geliştirilmiş İş Birliği**: Ekipler arasında daha iyi iş birliği ve sorumluluk paylaşımı sağlama.
- **Güvenlik**: Hızlı hareket ederken güvenlik ve uyumluluğu koruma.

## DevOps Yaşam Döngüsü ve Nasıl Çalışır?
DevOps yaşam döngüsü, yazılım geliştirme sürecinin başından sonuna kadar olan aşamaları kapsar:
- **Plan**: Yapılması gereken işleri organize etme, önceliklendirme ve tamamlanmasını takip etme.
- **Create (Oluşturma)**: Kod yazma, tasarlama, geliştirme ve proje verilerini yönetme.
- **Verify (Doğrulama)**: Kodun doğru çalıştığını ve kalite standartlarına uygun olduğunu doğrulama, genellikle otomatik testlerle.
- **Package (Paketleme)**: Uygulamaları ve bağımlılıkları paketleme, konteynerleri yönetme ve artefaktları oluşturma.
- **Secure (Güvenlik)**: Güvenlik açıklarını statik ve dinamik testlerle tarama, fuzz testi ve bağımlılık taramaları yapma.
- **Release (Yayınlama)**: Yazılımı son kullanıcılara dağıtma.
- **Configure (Yapılandırma)**: Uygulamaları desteklemek için gerekli altyapıyı yönetme ve yapılandırma.
- **Monitor (İzleme)**: Performans metriklerini ve hataları izleme, olayların şiddetini ve sıklığını azaltmaya yardımcı olma.
- **Govern (Yönetim)**: Güvenlik açıklarını, politikaları ve uyumluluğu yönetme.

## DevOps Araçları, Kavramlar ve Temel Bilgiler
- **Version Control**: Kaynak kod ve diğer dosyalar üzerinde yapılan her değişikliği izleme ve yönetme.
- **Continuous Integration - CI**: Tüm kod değişikliklerini ana dal ile düzenli olarak entegre etme, her değişikliği otomatik olarak test etme.
- **Continuous Delivery - CD**: Sürekli entegrasyon ile birlikte, altyapı tedarikini ve uygulama dağıtım sürecini otomatikleştirme.
- **Shift Left**: Güvenlik ve test süreçlerini geliştirme sürecinin çok daha erken safhalarına kaydırma, bu sayede geliştirme sürecini hızlandırırken kod kalitesini de artırma.

## DevOps Engineer/Consultant Kimdir?
- **DevOps Engineer/Consultant**: Yazılım geliştirme yaşam döngüsünün tüm yönlerinden sorumlu olan, iş akışlarına geliştirme süreçlerini etkin bir şekilde entegre eden, otomasyon ve test süreçlerini tanıtan ve analiz eden, ve IT altyapısını yöneten kişidir.

# Git Nedir?

**Git**, dağıtık bir versiyon kontrol sistemi olarak tanımlanır. Birden fazla geliştiricinin aynı proje üzerinde aynı anda çalışmasını sağlar. Her geliştirici, projenin tüm geçmişini içeren yerel bir kopyaya sahiptir.

# Deployment Methods

Geliştirme ortamlarından üretim ortamlarına uygulamaların güvenli ve sorunsuz bir şekilde dağıtılması, başarılı bir DevOps sürecinin kritik bir parçasıdır. İşte kullanılan bazı temel deployment yöntemleri:

## Blue/Green Deployment
**Blue/Green Deployment**, yük dengeleyiciye dayalı bir dağıtım stratejisidir. Bu yöntemde, aynı uygulamanın iki versiyonu (Blue ve Green) paralel olarak çalıştırılır.

### İşleyişi:
- **Blue Sunucuları**: Mevcut üretim sürümünü çalıştıran sunuculardır.
- **Green Sunucuları**: Yeni sürümü barındıran sunuculardır.

### Adımlar:
1. **Yeni Sürüm Dağıtımı**: Yeni sürüm (v1.2), Green sunuculara dağıtılır ve bu sunucular üzerinde test edilir.
2. **Geçiş**: Herhangi bir sorun yoksa, yük dengeleyici trafiği Blue sunucularından Green sunucularına yönlendirir.
3. **Geri Alma Seçeneği**: Eğer sorun oluşursa, yük dengeleyici tekrar Blue sunucularına yönlendirilir.

### Avantajlar:
- Anında geri alma imkanı sağlar.
- Tüm kullanıcılar aynı anda yeni sürüme geçer, böylece tutarsızlıklar önlenir.
- Uygulama başlangıçtan sona kadar test edilebilir ve üretim ortamına geçmeden önce ortaya çıkan sorunlar giderilebilir.

### Dezavantajlar:
- İki kat sunucuya ihtiyaç duyulur, bu da maliyeti artırır.
- Green sunucuları Blue sunucularından farklı bir ortamda olabilir, bu da sistemi tamamen test etmeyi gerektirir.
- Durum bilgisi olan uygulamalarda, uygulama durumu korunmaz.

## Canary Release
**Canary Release**, Blue/Green Deployment'a benzer bir yöntemdir, ancak burada yeni sürüm rastgele bir kullanıcı grubuna sunulur.

### İşleyişi:
- Uygulamanın yeni sürümü (v1.2) belirli bir kullanıcı yüzdesine (örneğin, %10-15) sunulur.
- Uygulamanın gerçek ortamda nasıl çalıştığı izlenir.
- Eğer herhangi bir sorun gözlemlenmezse, yeni sürüm yavaş yavaş tüm kullanıcılara dağıtılır.

### Avantajlar:
- Gerçek kullanıcı geri bildirimlerini toplama imkanı sağlar.
- Yeni sürümün küçük bir grup tarafından test edilmesi, büyük çaplı sorunların önlenmesine yardımcı olabilir.

### Dezavantajlar:
- Daha karmaşık bir dağıtım ve izleme süreci gerektirir.
- Geri alma durumunda, belirli bir kullanıcı grubu etkilenmiş olabilir.

Bu yöntemler, yazılım güncellemelerinin kullanıcılar üzerinde minimum etkiyle nasıl yönetilebileceğine dair çeşitli stratejiler sunar. Hangi yöntemin seçileceği, uygulamanın yapısına, kullanıcı tabanına ve dağıtım gereksinimlerine bağlı olarak değişir.

# Branching Strategies

Branching stratejileri, DevOps'ta özelliklerin ve düzeltmelerin geliştirilmesi, test edilmesi ve dağıtılması süreçlerini sistematik ve verimli bir şekilde yönetmek için hayati öneme sahiptir. Projenin boyutuna, karmaşıklığına ve yayın döngüsüne bağlı olarak farklı dallanma stratejileri kullanılabilir. Aşağıda, DevOps'ta en yaygın olarak kullanılan dallanma stratejileri açıklanmaktadır.

## 1. Trunk-Based Development (Ana Branch Tabanlı Geliştirme)

Trunk-based development, geliştiricilerin değişikliklerini sık sık paylaşılan bir ana dala (trunk) entegre ettikleri bir versiyon kontrol yönetimi pratiğidir. Bu strateji, CI/CD (Sürekli Entegrasyon/Sürekli Teslimat) süreçleri için idealdir çünkü birleştirme ve entegrasyon aşamalarını hızlandırır. Trunk-based development, özellikle kod tabanı karmaşıklığı ve ekip büyüklüğü arttıkça üretim sürümlerinin akışını sağlar.

## 2. GitHub Flow

GitHub Flow, daha küçük ekipler veya birden fazla sürüm desteklemeyen web uygulamaları için kullanılan nispeten basit bir iş akışıdır. Bu stratejide, ana dal (main branch) üretim için hazır kodu içerir ve yeni çalışmalar için oluşturulan dallar (feature branches) tamamlandığında ve gözden geçirildiğinde ana dala geri birleştirilir. GitHub Flow, sürekli teslimat ve sürekli entegrasyon süreçlerini destekleyen basit bir iş akışı sunar.

### GitHub Flow'un Faydaları
- En basit dallanma stratejilerinden biridir.
- Sürekli Entegrasyon ve Sürekli Teslimat süreçleri için uygundur.
- Küçük ekipler ve web uygulamaları için idealdir.

### GitHub Flow'un Zorlukları
- Üretimde aynı anda birden fazla kod sürümünü destekleyemez.
- Geliştirme dallarının eksikliği, GitHub Flow'u üretimde hata yapma olasılığı daha yüksek hale getirir.

## 3. GitLab Flow

GitLab Flow, GitHub Flow'a benzer bir iş akışıdır ancak çevre dallarının (production ve pre-production) veya sürüm dallarının eklenmesiyle farklılık gösterir. GitLab Flow, iki farklı sürüm döngüsü ile çalışır: Versiyonlu Sürüm ve Sürekli Sürüm.

### GitLab Flow'un Faydaları
- GitHub Flow'a göre daha organize ve yapılandırılmıştır.
- Sürekli Teslimat ve versiyonlu sürümleri destekler.

### GitLab Flow'un Zorlukları
- En basit dallanma stratejisi değildir.
- Bazı durumlarda iş birliği karmaşık hale gelebilir.

## 4. GitFlow

GitFlow, çalışmaların farklı türde dallara ayrılmasını öngören bir dallanma stratejisidir. GitFlow'da beş farklı dal türü bulunur: Ana (main), Geliştirme (develop), Özellik (feature), Sürüm (release) ve Düzeltme (hotfix). Bu strateji, uzun bakım döngülerine sahip ürünler için uygundur.

### GitFlow'un Faydaları
- Büyük projelerde ve uzun sürüm döngülerinde iyi çalışır.
- Karmaşık sürüm yönetimi ve bakımı gerektiren projeler için uygundur.

### GitFlow'un Zorlukları
- Daha karmaşık bir iş akışı olduğu için küçük ekipler ve projeler için aşırı olabilir.
- Özellik dallarının uzun süre yaşaması, birleştirme sorunlarına yol açabilir.

## 5. Dallanma Stratejisi Seçimi

Her projenin ihtiyaçlarına göre en uygun dallanma stratejisi seçilmelidir. Örneğin:
- **Sürekli Dağıtım ve Yayın** için küçük ekipler GitHub Flow veya Trunk-Based Development kullanabilir.
- **Programlanmış ve Periyodik Sürüm** için orta büyüklükteki ekipler GitFlow veya GitLab Flow tercih edebilir.
- **Kaliteye odaklı sürekli dağıtım** gerektiren projeler için GitLab Flow uygundur.
- **Uzun bakım döngülerine sahip ürünler** için büyük ekipler GitFlow'u kullanabilir.

---

# 2. Gün - Git Giriş

Staj programımızın ikinci gününde Git hakkında detaylı bir giriş yapıldı. Git'in ne olduğu, nasıl kurulduğu ve temel komutlarının kullanımı üzerine yoğunlaştık. Git, dağıtık bir versiyon kontrol sistemi olarak özellikle yazılım geliştirme süreçlerinde çok kritik bir rol oynadığı anlatıldı.

## Git Nedir?
- Git, birden fazla geliştiricinin aynı proje üzerinde aynı anda çalışmasını sağlar. Her geliştirici, projenin tüm geçmişini içeren yerel bir kopyaya sahiptir.
- Git'in dallanma ve birleştirme özellikleri sayesinde, farklı özellikler veya düzeltmeler üzerinde bağımsız olarak çalışılabilir.
- Verilerin bütünlüğünü sağlamak için SHA-1 hash algoritması kullanılır, bu da verilerin güvenliğini artırır.

## Git'in Temel Komutları
- **git init**: Yeni bir Git deposu oluşturur.
- **git clone**: Var olan bir uzaktaki depoyu yerel makineye kopyalar.
- **git add**: Değişiklikleri sahnelemek için kullanılır.
- **git status**: Projede yapılan değişikliklerin durumunu gösterir.
- **git commit**: Sahnedeki değişiklikleri kaydeder.
- **git restore**: Çalışma dizininde belirtilen yolları geri yükler.
- **git branch**: Dalların yönetimi için kullanılır.
- **git checkout**: Dal değiştirmek veya bir dalı geri yüklemek için kullanılır.
- **git switch**: Farklı bir dala geçiş yapar.
- **git stash**: Çalışma dizinindeki geçici değişiklikleri saklar.
- **git tag**: Bir commit'e etiket ekler.
- **git fetch**: Uzak depodan yeni verileri alır.
- **git pull**: Uzak depodan verileri indirir ve yerel depoyla birleştirir.
- **git push**: Yerel değişiklikleri uzak depoya gönderir.
- **git remote**: Uzak depoların yönetimi için kullanılır.
- **git show**: Bir nesneyi gösterir (commit, tag, vs.).
- **git log**: Commit geçmişini gösterir.
- **git diff**: Çalışma dizini ve depodaki farkları gösterir.
- **git difftool**: Farkları karşılaştırmak ve düzenlemek için bir diff aracını kullanır.
- **git apply**: Diff çıktısını alır ve dosyalara uygular.
- **git cherry-pick**: Bir commit'i mevcut dala uygular.
- **git rebase**: Bir dalın tabanını yeniden konumlandırır.
- **git revert**: Bir commit'in yaptığı değişiklikleri geri alır.
- **git bisect**: Bir hatayı tanımlamak için iki commit arasında binary arama yapar.
- **git blame**: Bir dosyanın satırlarının son kim tarafından değiştirildiğini gösterir.
- **git grep**: Dosyalarda belirtilen desenleri arar.
- **gitattributes**: Dosya özniteliklerini tanımlar.
- **gitignore**: Takip edilmemesi gereken dosyaları belirler.
- **git security - SSH**: SSH anahtarları kullanarak güvenli bağlantı sağlar.
- **git security - Generate SSH Key Pair**: SSH anahtar çiftini oluşturur.

## Git Basics – Tracking Statuses
- **Untracked**: Git henüz dosyayı izlemiyor. Bu, dosyanın henüz bir commite eklenmediği ve Git'in şu anda bu dosyadaki değişiklikleri izlemediği anlamına gelir.
- **Unmodified**: Dosya, son committen bu yana değiştirilmedi.
- **Modified**: Dosya değiştirildi ancak commit için sahnelenmedi. Dosyada değişiklikler yapılmış ancak bu değişiklikler henüz bir sonraki commite dahil edilmemiştir.
- **Staged**: Dosyanın değişiklikleri bir sonraki commit için sahnelendi. Bu, değişikliklerin bir sonraki commite dahil edilmek üzere işaretlendiği anlamına gelir.

## Git Basics – Tracking Flow
Git'in temel takip akışı aşağıdaki gibidir:
1. Yeni dosyalar oluşturulduğunda, bu dosyalar "untracked" durumundadır.
2. `git add` komutu ile dosyalar "staged" duruma geçer.
3. `git commit` komutu ile "staged" durumdaki dosyalar commit edilir ve "unmodified" duruma geçer.
4. Dosyalar üzerinde yapılan değişiklikler, bu dosyaları "modified" duruma getirir.
5. Değişiklikler tekrar `git add` ile "staged" duruma getirilir ve süreç bu şekilde devam eder.


# 2. Gün - Linux, Shell Scripting & Bash Scripting

Staj programımızın ikinci gününde ayrıca Linux ve Shell Scripting konularını da ele aldık. Linux ortamında sistem yönetimi ve otomasyon görevleri için temel olan bu konular, özellikle DevOps süreçlerinde kritik bir rol oynuyor.

## Linux & Shell Scripting Nedir?
- **Linux**: Açık kaynaklı bir işletim sistemidir ve sunucular, masaüstü bilgisayarlar ve gömülü sistemler dahil olmak üzere çeşitli platformlarda yaygın olarak kullanılır.
- **Shell**: Shell, işletim sistemi ile etkileşim kurmamızı sağlayan bir arayüzdür. Kullanıcı komutlarını alır, işler ve sonucu döndürür. Linux'ta yaygın olarak kullanılan shell türleri arasında Bash, Zsh ve Fish bulunur.

## Shell Scripting Neden Önemlidir?
- Shell scripting, bir dizi komutun bir dosyada toplanarak otomatik olarak çalıştırılmasını sağlar. Bu sayede tekrarlayan görevler kolayca otomatikleştirilebilir ve zamandan tasarruf sağlanabilir.
- **Örnek Kullanım Alanları**:
  - Kullanıcı hesaplarının oluşturulması.
  - Sistem başlatma script'lerinin yazılması.
  - Otomatik yedekleme ve geri yükleme işlemleri.

## Linux ve Shell Scripting Temel Komutları
### Dosya ve Dizin İşlemleri:
- **`pwd`**: Mevcut çalışma dizinini gösterir.
- **`cd`**: Dizinler arasında geçiş yapar.
- **`ls`**: Mevcut dizindeki dosyaları listeler.
- **`mkdir`**: Yeni bir dizin oluşturur.
- **`touch`**: Yeni bir dosya oluşturur.
- **`rm`**: Dosya ve dizinleri siler.
- **`cp`**: Dosyaları kopyalar.
- **`mv`**: Dosyaları taşır veya yeniden adlandırır.

### Dosya ve Dizin Navigasyonu:
- **Yol İsimleri**:
  - **Absolute Path**: Köklü dizinden başlayan tam yol.
  - **Relative Path**: Mevcut dizine göre belirtilen yol.

- **Özel Karakterler**:
  - `/`: Dizin ayracı.
  - `\`: Kaçış karakteri.
  - `#`: Yorum satırı.
  - `*`: Belirtilen şablonla eşleşen tüm dosyalar.

## Bash Scripting
### Bash Script Yazımı:
- Bash script'leri `.sh` uzantısıyla kaydedilir ve komut satırında `./script_ismi.sh` komutuyla çalıştırılır.
- **Örnek Bash Script**:
    ```bash
    #!/bin/bash
    echo "Merhaba, dünya!"
    ```

### Bash Komutları ve Kullanımı:
- **Echo**: Komut satırına yazdırma yapar.
  ```bash
  echo "Merhaba, dünya!"

- **Clear**: Ekranı temizler.
    ```bash
    clear
    ```

- **Sleep**: Belirtilen süre kadar bekler.
    ```bash
    sleep 5
    ```

### Meta Bilgi Alma:
- Varsayılan shell interpreter'ını öğrenmek için:
    ```bash
    ps $$
    ```

- Bash yolunu öğrenmek için:
    ```bash
    which bash
    ```

### Komut Satırı Arayüzü:
- **İlk Komutunuz**:
    - `whoami`: Mevcut oturumun sahibinin kullanıcı adını döndürür.

### Sık Kullanılan Komutlar:
- **`echo`**: Terminale metin yazdırır.
- **`clear`**: Terminali temizler.
- **`sleep`**: Komutu belirli bir süre geciktirir.

### Dosya ve Dizin İşlemleri:
- **`ls`**: Dizin içeriğini listeler.
- **`mkdir`**: Yeni bir dizin oluşturur.
- **`rm`**: Dosya veya dizinleri siler.

### Dosya Manipülasyonu:
- **`touch`**: Yeni dosya oluşturur veya mevcut dosyanın zaman damgasını günceller.
- **`cat`**: Dosya içeriğini görüntüler.
- **`mv`**: Dosya veya dizinleri taşır veya yeniden adlandırır.
- **`cp`**: Dosya veya dizinleri kopyalar.


# 3. Gün - Ağ 101 (Network 101)

Staj programımızın üçüncü gününde temel ağ (network) kavramlarını ve yapılarını ele aldık.

## Ağ Nedir?
- **Ağ (Network)**: Ağ, ağ cihazlarının birbiriyle iletişim kurabildiği ve kaynaklarını paylaşabildiği bir ortamdır. Bu iletişim, küçük bir alanda (örneğin bir apartman içi) veya daha geniş mesafelerde (örneğin farklı şehirler arasında) gerçekleşebilir.

## Ağ Topolojileri
- **LAN (Local Area Network)**: Küçük bir alan içinde bulunan ağlar. Örnek: Bir apartman içindeki ağ.
- **MAN (Metropolitan Area Network)**: Bir şehir içindeki ağlar. Örnek: Bir şehir içindeki ağ bağlantıları.
- **WAN (Wide Area Network)**: Farklı şehirler veya ülkeler arasında kurulan ağlar. Örnek: Farklı şehirler arasındaki ağ bağlantıları.

## OSI Katmanları
- OSI referans modeli, katmanlı bir yapıda çalışır. Her katman, üst katmana hizmet sağlar. İki bilgisayarın ağ üzerinden iletişim kurarken, katmanlar sırasıyla iletişim kurar.
- **Fiziksel Katman (Physical Layer)**: Verilerin kablo üzerindeki yapısını belirler. Veriler bitler halinde iletilir. Gönderici tarafta, fiziksel katman 1 ve 0'ları elektriksel sinyallere dönüştürür ve kabloya yerleştirir.
- **Veri Bağı Katmanı (Data Link Layer)**: Fiziksel katmana erişim ve kullanım kurallarını belirler. Veri bağı katmanı, ağ üzerindeki diğer bilgisayarları tanımlar, kabloyu kimin kullandığını belirler ve fiziksel katmandan gelen verileri hatalara karşı kontrol eder.
- **Ağ Katmanı (Network Layer)**: Veriyi kaynaktan alıcıya farklı bir ağda iletmekten sorumludur ve kaynak ile hedef için bir adresleme mekanizması sağlar. Bu katmanda adresler IP adresleridir.

## IP Adresi
- **IP Adresi**: TCP/IP protokolünü kullanarak internet veya diğer paket anahtarlamalı ağlara bağlı cihazların birbirleriyle veri alışverişi yapmasını sağlayan adrestir. IP adresi, cihazların birbirleriyle iletişim kurabilmesi için her cihaza atanır.
- Günümüzde **IPv4** kullanılıyor, ancak yakında **IPv6**'ya geçilecek. IPv4, 2^32 cihazı adreslerken, IPv6 2^128 cihazı adresleyebilir.

## Alt Ağ Maskesi (Subnet Mask)
- **Subnet Mask**: IP adreslerini daha küçük alt ağlara bölmek için kullanılan bir araçtır. Ağ yönetiminde önemli bir rol oynar ve IP adreslerinin hangi kısmının ağ adresini, hangi kısmının ise host adresini temsil ettiğini belirler. Örneğin, 192.168.1.10 IP adresi ve 255.255.255.0 alt ağ maskesi ile ağ adresi 192.168.1.0, ve bu ağdaki hostlar 192.168.1.1 - 192.168.1.254 aralığında yer alır.

## Ağ Geçidi (Gateway)
- **Ağ Geçidi (Gateway)**: Bir ağ üzerindeki cihazların diğer ağlarla iletişim kurmasını sağlayan bir ağ cihazıdır. Genellikle bir router olarak işlev görür ve farklı ağ segmentleri veya ağlar arasında veri paketlerini iletir.

## Taşıma Katmanı (Transport Layer)
- **Taşıma Katmanı (Transport Layer)**: Üst katmanlardan gelen verileri, ağ paket boyutuna göre parçalara böler. Bu katmanda veriler segmentler halinde taşınır. TCP ve UDP protokolleri bu katmanda çalışır. TCP, iki bilgisayar arasında bağlantı kurmayı sağlar ve bu bağlantı **Üç Yönlü El Sıkışma (Three-Way Handshake)** yöntemiyle gerçekleştirilir.

## Port Numaraları
- **Port Numaraları**: Bir bilgisayar ağında veri iletişimini organize etmek için kullanılır ve bir cihazdaki belirli bir uygulama veya hizmet ile ilişkilidir. IP adresleri cihazları tanımlarken, port numaraları bu cihazlardaki belirli süreçleri veya uygulamaları tanımlar. Örneğin, 80 (http), 443 (https) gibi yaygın portlar vardır.

## OSI Modelinin Diğer Katmanları
- **Oturum Katmanı (Session Layer)**: Bir bilgisayarın aynı anda birden fazla bilgisayar ile iletişim kurmasını sağlar.
- **Sunum Katmanı (Presentation Layer)**: Gönderilen verilerin diğer bilgisayar tarafından anlaşılmasını sağlar.
- **Uygulama Katmanı (Application Layer)**: Bilgisayar uygulaması ile ağ arasında bir arayüz sağlar. SSH, telnet, FTP, HTTP, DNS gibi protokoller bu katmanda çalışır.

## DNS (Domain Name Server)
- **DNS**: İnternetin telefon rehberi olarak adlandırılır. Her cihazın internet üzerinde benzersiz bir IP adresi vardır ve DNS, bu IP adreslerini insanın daha kolay hatırlayabileceği alan adlarına çevirir. Örneğin, 192.168.23.202 IP adresi "my-example.com" gibi bir alan adına çevrilebilir.

### DNS Kayıt Türleri
- **A Kayıtları (A Record)**: Bir adı bilinen ve sabit IP adreslerine eşler.
- **CNAME Kayıtları (CNAME Record)**: Bir adı başka bir ada eşler. Başka kayıtların olmadığı durumlarda kullanılmalıdır.

---

# 4. Gün - Python Temelleri ve Veri Bilimine Giriş

Staj programımızın dördüncü gününde Python programlama dili ve veri bilimi temel kavramları üzerinde durduk. Python, veri bilimi ve makine öğrenimi gibi alanlarda en çok tercih edilen programlama dillerinden biridir.

## Python Temelleri
### Basit Hesap Makinesi
Verilen bir ifade dizisini temsil eden bir string kullanarak, temel matematiksel işlemleri gerçekleştiren bir hesap makinesi. Örnek olarak:
- **Girdi**: `s = "1 + 1"`
- **Çıktı**: `2`
- **Çözüm**:
    ```python
    def calculator(expression):
        number = 0
        sign_value = 1
        result = 0
        operations_stack = []
        for c in expression:
            if c.isdigit():
                number = number * 10 + int(c)
            if c in "+-":
                result += number * sign_value
                sign_value = -1 if c == '-' else 1
                number = 0
            elif c == '(':
                operations_stack.append(result)
                operations_stack.append(sign_value)
                result = 0
                sign_value = 1
            elif c == ')':
                result += sign_value * number
                result *= operations_stack.pop()
                result += operations_stack.pop()
                number = 0
        return result + number * sign_value
    ```

### Roma Rakamlarından Tam Sayıya Çevirme
Roma rakamlarını tam sayılara dönüştüren bir algoritma üzerinde çalıştık. Roma rakamları, çeşitli sembollerin bir araya gelmesiyle oluşur. Örnek:
- **Girdi**: `s = "MCMXCIV"`
- **Çıktı**: `1994`
- **Çözüm**:
    ```python
    def romanToInt(self, s: str) -> int:
        val_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        prev_roman = 0
        for letter in s:
            if prev_roman < val_dict[letter]:
                num -= prev_roman * 2
            num += val_dict[letter]
            prev_roman = val_dict[letter]
        return num
    ```

## Veri Bilimine Giriş
### Veri Bilimi ve İlgili Alanlar
Veri bilimi, verilerden geleceğe yönelik tahminlerde bulunmak için içgörüler çıkarmayı içerir. Veri mühendisliği, veri analizi ve veri bilimi arasındaki farkları öğrendik.

### Veri Bilimi Yaşam Döngüsü
Veri bilimi yaşam döngüsü, problem anlama ile başlar ve modelleme ve izleme ile son bulur. Temel aşamalar:
1. **Problem Anlama**: Sorunu ve sorulması gereken soruları anlamak.
2. **Veri Toplama**: İlgili verileri toplamak.
3. **Veri Temizleme**: Verilerin işlenmeye uygun hale getirilmesi.
4. **Veri Keşfi**: Görselleştirme ve diğer istatistiksel yöntemlerle veri üzerinde incelemeler yapmak.
5. **Özellik Mühendisliği**: Modelleme öncesi veriyi işlemek.
6. **Modelleme**: Verilerin anlamını ortaya çıkarmak için modeller oluşturmak.
7. **Model Dağıtımı**: Modeli gerçek dünyada kullanıma sunmak.
8. **İzleme**: Model performansını izlemek ve gerekirse iyileştirmek.

### Yapılandırılmış, Yarı Yapılandırılmış ve Yapılandırılmamış Veri
- **Yapılandırılmış Veri**: Önceden belirlenmiş bir formatı vardır ve genellikle ilişkisel veritabanlarında saklanır.
- **Yarı Yapılandırılmış Veri**: JSON veya XML gibi bir formatı vardır ancak ilişkisel veritabanlarında saklanmaz.
- **Yapılandırılmamış Veri**: Belirli bir formatı yoktur. Örneğin, resimler, videolar, konuşma kayıtları gibi.

## Python Kütüphaneleri
### Beautiful Soup ve Scrapy
- **Beautiful Soup**: Web sayfalarından veri çekmek için kullanılan bir Python kütüphanesidir.
- **Scrapy**: Daha organize bir yapı ile veri kazıma işlemleri için kullanılır.

### Numpy ve Pandas
- **Numpy**: Matrisler ve çok boyutlu diziler üzerinde hızlı ve verimli işlemler yapmamızı sağlar.
- **Pandas**: Veri yapıları sunar ve bu yapılar üzerinde veri analizi ve işleme işlemleri gerçekleştirilir.

## Makine Öğrenimi
### Denetimli ve Denetimsiz Öğrenme
- **Denetimli Öğrenme**: Etiketlenmiş veri kullanarak modeli eğitme.
- **Denetimsiz Öğrenme**: Etiketlenmemiş veri üzerinde deseni öğrenme.

## Derin Öğrenme (Deep Learning)
- **Derin Öğrenme**: Makine öğreniminin bir alt dalıdır ve yapay sinir ağlarını kullanarak problemleri ele alır. Yapay sinir ağları, insan beyninin çalışma prensiplerinden esinlenmiştir. Derin öğrenme yöntemleri, klasik makine öğrenimi yöntemlerine göre birçok avantaj sağlar.
- **Yapay Sinir Ağları**: Bir sinir ağı, giriş katmanı, gizli katman ve çıkış katmanı olmak üzere üç ana kısımdan oluşur. Pytorch ve Tensorflow, yapay sinir ağları oluşturmak için kullanılan popüler kütüphanelerdendir .

## Regresyon Nedir?

Regresyon, istatistik ve makine öğreniminde, bir bağımlı değişken (hedef değişken) ile bir veya daha fazla bağımsız değişken (girdi değişkenleri) arasındaki ilişkiyi modelleyen bir tekniktir. Regresyon analizi, bu ilişkiyi belirlemek ve tahmin yapmak için kullanılır. Regresyon, veri noktaları arasındaki ilişkiyi açıklamak, bu ilişkiyi bir matematiksel modelle ifade etmek ve gelecekteki veriler için tahminlerde bulunmak amacıyla kullanılır.

## Regresyon Çeşitleri
### Basit Doğrusal Regresyon (Univariate Linear Regression)
- **Basit Doğrusal Regresyon**: Bir bağımsız değişken kullanılarak bağımlı bir değişkenin tahmin edilmesi sürecidir. Model, bağımsız değişken ile bağımlı değişken arasındaki doğrusal ilişkiyi tanımlayan bir denklemi oluşturur .

### Multivariate Linear Regression
- **Multivariate Linear Regression**: Birden fazla bağımsız değişken kullanılarak bağımlı bir değişkenin tahmin edilmesidir. Bu yöntem, daha karmaşık veri setlerinde kullanılmak üzere tasarlanmıştır ve birden fazla girdiyi hesaba katar  .

### Regularization
- **Ridge Regresyon**: L2 düzenlemesi olarak da bilinen Ridge regresyon, aşırı öğrenmeyi (overfitting) azaltmak için maliyet fonksiyonuna bir ceza terimi ekler.
- **Lasso Regresyon**: L1 düzenlemesi olarak da bilinen Lasso regresyon, özellik seçiminde de kullanılan bir yöntemdir. Bazı model parametrelerini sıfıra çekerek sade bir model oluşturur.
- **Elastic Net Regresyon**: Hem L1 hem de L2 düzenlemesini bir araya getiren bir yöntemdir. Ridge ve Lasso regresyonlarının avantajlarını birleştirir .

## Feature Scaling
- **Feature Scaling**: Veri setindeki özelliklerin normalize edilmesi işlemidir. Birçok makine öğrenimi algoritması, özelliklerin ölçeğinden etkilenir ve bu nedenle verilerin ölçeklendirilmesi gerekir.
    - **Normalization**: Özelliklerin 0 ile 1 arasına yeniden ölçeklendirilmesidir.
    - **Standardization**: Özelliklerin ortalaması 0 ve standart sapması 1 olacak şekilde yeniden ölçeklendirilmesidir  .

## Model Evaluation
- **Model Evaluation**: Bir modelin performansını değerlendirmek için kullanılan çeşitli metrikler vardır. Bu metrikler, modelin eğitim verisi üzerinde ne kadar iyi performans gösterdiğini ve genelleme yeteneğini ölçer.
    - **Mean Absolute Error (MAE)**: Tahmin edilen değerler ile gerçek değerler arasındaki ortalama mutlak hatadır.
    - **Mean Squared Error (MSE)**: Tahmin edilen değerler ile gerçek değerler arasındaki ortalama kare hatadır.
    - **R² Skoru**: Modelin açıklama gücünü ölçen bir metriktir, 1.0 en iyi skordur .

## Cross Validation
- **Cross Validation**: Modelin genelleme yeteneğini değerlendirmek için kullanılan bir tekniktir. Veri seti belirli katmanlara bölünür ve her katman bir test seti olarak kullanılırken diğerleri eğitim için kullanılır. Bu işlem, modelin farklı veri setleri üzerindeki performansını ölçer .

## Classification
- **Lojistik Regresyon (Logistic Regression)**: İki kategorili sonuçları tahmin etmek için kullanılan bir regresyon türüdür. Örneğin, hastanın hasta olup olmadığını tahmin etmek gibi.
- **Destek Vektör Makineleri (Support Vector Machines)**: Verileri sınıflandırmak için kullanılan bir algoritmadır. Veri seti içindeki sınıflar arasındaki en iyi sınırı bulur.
- **Karar Ağaçları (Decision Trees)**: Veriyi sınıflandırmak için ağaç yapısında bir model oluşturur. Her dal, bir özelliğe dayalı olarak bir kararı temsil eder :contentReference[oaicite:0]{index=0}.

## Hyper-Parameter Optimization
- **Grid Search & Random Search**: Hiperparametreleri ayarlamak için kullanılan yöntemlerdir. Grid Search, belirli bir parametre ızgarasındaki tüm kombinasyonları denerken, Random Search rastgele kombinasyonları dener.
- **Open Source Tools**: Hiperparametre optimizasyonu için kullanılan açık kaynak araçlar arasında Hyperopt ve Optuna yer alır .

## Titanic - Machine Learning from Disaster
- **Titanic Veri Seti**: Bu veri seti, Titanic kazasında hayatta kalanları tahmin etmek için kullanılır. Makine öğrenimi modelleri geliştirmek için popüler bir yarışma veri setidir. Bu proje, öğrendiklerimizi uygulamak ve model geliştirme sürecini deneyimlemek için kullanıldı .

---
# 5. Gün - MLOps ve MLflow

Staj programımızın beşinci gününde MLOps (Machine Learning Operations) ve MLflow ile ilgili önemli kavramlar üzerinde durduk. Bu konular, makine öğrenimi modellerinin geliştirilmesi, izlenmesi ve yönetilmesi için kritik öneme sahiptir.

## MLOps Nedir?
- **MLOps**: MLOps, makine öğrenimi operasyonlarını ifade eden bir kavramdır. MLOps, makine öğrenimi modellerinin geliştirilmesinden üretime alınmasına kadar olan süreçleri kapsar. DevOps'tan ilham alır, ancak veri bilimi ve makine öğrenimi alanına özgü zorluklarla başa çıkmak için özel olarak tasarlanmıştır.

### DevOps ve MLOps Arasındaki Farklar
- **DevOps vs MLOps**: DevOps yazılım geliştirme ve IT operasyonlarını birleştirirken, MLOps, makine öğrenimi modellerini yönetir. Veri bilimciler, yazılım geliştiricilerinden farklı bir teknik geçmişe sahiptir ve MLOps, bu iki alanı birleştirir.

## MLflow Nedir?
- **MLflow**: MLflow, makine öğrenimi iş akışlarını yönetmek için kullanılan açık kaynaklı bir platformdur. MLflow, deneyleri takip etme, modelleri kaydetme ve dağıtma, model yaşam döngüsünü yönetme gibi işlevler sunar. MLflow dört ana bileşenden oluşur:
  - **Tracking**: Model eğitim oturumlarını kaydeder ve izler.
  - **Projects**: Veri bilimi projelerini paketler ve tekrarlanabilirliği sağlar.
  - **Models**: Modelleri paketler ve yeniden kullanılabilir hale getirir.
  - **Model Registry**: Modellerin yaşam döngüsünü merkezi olarak yönetir.

### MLflow UI
- **MLflow UI**: MLflow'un kullanıcı arayüzü, deneylerin ve modellerin görselleştirilmesini sağlar. Bu arayüz, farklı çalışmaları izlemek ve karşılaştırmak için kullanılır.

### Model Deneyleri (Model Experiments)
- **Model Experiments**: MLflow, farklı modellerin ve hiperparametre kombinasyonlarının izlenmesini ve karşılaştırılmasını sağlar. Deneylerin takibi, hangi yapılandırmaların en iyi sonuçları verdiğini anlamayı kolaylaştırır.

### Deney Takibi (Tracking Experiments)
- **Tracking**: MLflow'un takip bileşeni, deneylerinizi kaydetmenizi ve sorgulamanızı sağlar. Hiperparametreler, metrikler ve model çıktıları gibi tüm önemli bilgileri kaydedebilir ve karşılaştırabilirsiniz.

### Parameters ve Artifacts Loglanması
- **Log Parameters**: Hiperparametreler ve metrikler gibi deneyler sırasında elde edilen bilgileri kaydetme işlemi.
- **Log Artifacts**: Eğitim sırasında oluşturulan dosyalar veya modeller gibi artifaktların loglanması.

### Model Registry
- **Model Registry**: MLflow Model Registry, modelleri ve bu modellerin yaşam döngüsünü merkezi olarak yönetmek için bir API ve kullanıcı arayüzü sağlar. Model sürümlendirme, anotasyonlar ve geçiş aşamaları bu bileşenin bir parçasıdır.

### Pipeline ve GitLab Entegrasyonu
- **Pipelines**: GitLab MLOps demo gösterisinde, modellerin nasıl pipeline’lar ile entegre edilip yönetilebileceği üzerinde duruldu. Pipeline'lar, model geliştirme süreçlerini otomatize etmek için kritik öneme sahiptir.

---

# 6. Gün - Konteynerleştirme ve Konteyner Yönetimi Temelleri

Staj programımızın altıncı gününde konteynerleştirme kavramları ve konteyner yönetimi temelleri üzerinde durduk. Konteynerler, modern yazılım geliştirme ve dağıtım süreçlerinde kritik bir rol oynamaktadır.

## Konteyner Kavramları
### Konteyner Nedir?
- **Konteynerler**, yalnızca uygulamaları ve bu uygulamaların bağımlılıklarını içeren hafif, taşınabilir ve izole edilmiş yazılım paketleridir. Masaüstü bilgisayarlardan bulut platformlarına kadar her yerde çalıştırılabilirler.

### Neden Konteynerler?
- **Taşınabilirlik**: Konteynerler, masaüstünden bulut altyapısına kadar her yerde çalıştırılabilir.
- **İzolasyon**: Konteynerler, içeriğini ana sistemden ve diğer konteynerlerden izole eder, bu da kararlılığı artırır ve güvenliği sağlar.
- **Verimlilik**: Konteynerler, sanal makineler gibi bir işletim sistemi içermez, bu da daha az kaynak kullanımı sağlar.
- **Tutarlılık**: Konteynerler, aynı ortamı yeniden üretir, bu da uygulamanın geliştirme, test ve üretim ortamlarında aynı şekilde davranmasını sağlar.
- **Ölçeklenebilirlik**: Konteynerler kolayca çoğaltılabilir ve ölçeklenebilir.
- **Sürüm Kontrolü**: Bağımlılık paketlerinin sürümünü tanımlamak ve sürümleri yönetmek mümkündür.
- **Kullanım Kolaylığı**: Konteynerler, CI/CD süreçlerinde kolayca oluşturulabilir, dağıtılabilir, depolanabilir ve geri alınabilir.

## Konteyner Mimarisi
- **Konteyner Mimarisi**: Konteynerler, ana işletim sisteminin çekirdeğini paylaşır, bu da onları sanal makinelerden daha hafif hale getirir. Konteynerlerin içerdiği uygulamalar, bağımsız olarak çalışabilir ve farklı ortamlar arasında taşınabilir.

### Sanal Makine (VM) Mimarisi ile Karşılaştırma
- **Konteynerler**: Ana işletim sisteminin çekirdeğini paylaşır, hafiftir ve hızlı başlatılabilir.
- **Sanal Makineler**: Her biri kendi işletim sistemi örneğini içerir, daha ağırdır ve başlatılması daha uzun sürer.

## Konteyner Terminolojisi ve Teknolojileri
- **CRI (Container Runtime Interface)**: Konteyner çalışma zamanı ve orkestrasyon platformlarının birlikte çalışmasını sağlayan standart işlemleri tanımlar.
- **Orchestrator (Orkestratör)**: Konteyner yaşam döngüsünü otomatikleştiren araçlardır, örneğin Kubernetes.
- **Docker**: En popüler konteyner teknolojisidir. DockerHub, en büyük konteyner kullanım payına sahiptir.
- **CRI-O, Containerd, Microsoft Containers**: Diğer konteyner teknolojileri arasında yer alır.

## Konteyner Yaşam Döngüsü
### Konteyner İşlemleri ve Oluşturma
- **Dockerfile Sözdizimi**:
  - `FROM`: Temel imaj.
  - `ENV`: Ortam değişkeni.
  - `WORKDIR`: Çalışma dizini.
  - `RUN`: İşletim sistemi komutu.
  - `ENTRYPOINT`: Giriş noktası.
  - `CMD`: Komut.
  - `COPY`: Dosyaları imaja kopyalar.
  - `ADD`: Dosyaları kopyalar, tar dosyalarını açabilir veya URL'den kaynak indirebilir.
  - `EXPOSE`: Dinlenecek port bilgisi.

### Konteyner İmajları Katmanlama
- **İmajların Katmanlanması**: Docker, önceden oluşturulmuş imajları kullanarak uygulamaların üzerine katman eklemeye izin verir. `FROM` anahtar kelimesi kullanılarak bir temel imaj seçilebilir.

## Docker Ağ Yönetimi
### Docker Ağ Türleri
- **Bridge**: Varsayılan ağ sürücüsü. Aynı ana bilgisayarda çalışan konteynerler arasındaki iletişim için kullanılır.
- **Host**: Konteyner ile Docker ana bilgisayarı arasındaki ağ izolasyonunu kaldırır.
- **Overlay**: Birden fazla Docker daemon'u birbirine bağlar ve Swarm hizmetleri ile konteynerlerin farklı düğümler arasında iletişim kurmasını sağlar.
- **IPVLAN**: Kullanıcılara IPv4 ve IPv6 adresleme üzerinde tam kontrol sağlar.
- **MACVLAN**: Bir konteynere MAC adresi atayarak, onu ağda fiziksel bir cihaz gibi görünür hale getirir.

## Docker Depolama
### Docker Depolama Seçenekleri
- **TMPFS Mounts**: Geçici dosya sistemi bağlamaları, yalnızca ana bilgisayar belleğinde kalıcıdır.
- **Volume Mounts**: Veri kalıcılığı için tercih edilen mekanizmadır. Docker tarafından yönetilir.
- **Bind Mounts**: Sınırlı işlevselliğe sahiptir, bir ana bilgisayar dosya veya dizini konteyner içine monte edilir.

## Docker Compose ve Konteyner Yönetimi
- **Docker Compose**: Birden fazla konteyneri yönetmek ve tanımlamak için kullanılır. Tüm hizmetler, `docker-compose.yml` dosyasında tanımlanır.
- **Docker Compose Yapılandırması**: `docker-compose.yml` dosyasında hizmetler, ağlar ve veri hacimleri tanımlanır.

### Konteyner Yönetimi
- **Health Checks**: Konteynerlerin çalışır durumda olup olmadığını izler ve bu bilgiyi ölçeklendirme, yük dengeleme ve hata toleransı sağlamak için kullanır.
- **Scaling (Ölçeklendirme)**: Konteynerlerin çoğaltılmasıyla iş yükü dengelenir. Dikey ve yatay ölçeklendirme yöntemleri bulunur.
  - **Dikey Ölçeklendirme**: Bir konteynere kaynak ekleyerek performansı artırmak.
  - **Yatay Ölçeklendirme**: Daha fazla konteyner örneği ekleyerek iş yükünü azaltmak.
- **Deployment (Dağıtım)**: Uygulamanın konteynere yerleştirilmesi ve hedef ortamda çalıştırılması. Genellikle Kubernetes kümesi üzerinde gerçekleştirilir.
- **Load Balancing (Yük Dengeleme)**: Gelen istekleri birden fazla hedef arasında dengeler, uygulama performansını artırır ve hizmet sürekliliğini sağlar.
  - **Yük Dengeleme Algoritmaları**: Round Robin, En Az Bağlantı, IP Hashing, En Yakın Sunucu gibi algoritmalar kullanılır.


---
# 7. Gün - Cloud Computing & Infrastructure Management

Staj programımızın yedinci gününde bulut bilişim ve altyapı yönetimi konularını inceledik. Bu bağlamda, özellikle Infrastructure as Code (IaC) kavramı ve Terraform aracı üzerinde durduk.

## Infrastructure as Code (IaC) Nedir?
- **Infrastructure as Code (IaC)**: Altyapıyı manuel işlemler yerine kod kullanarak sağlama ve destekleme yeteneğidir. Uygulama ortamları, işletim sistemleri, veri tabanı bağlantıları ve depolama gibi birçok altyapı bileşeni gerektirir. IaC, bu altyapıyı tanımlanmış bir kodla otomatik olarak yönetir, böylece geliştiriciler ortamları yönetmek yerine uygulamalar oluşturma ve iyileştirme çalışmalarına odaklanabilirler.

### IaC'nin Faydaları
- **Otomasyon**: Altyapı otomasyonu ile ortamlar hızlıca kurulabilir. Yazılım geliştirme, test ve dağıtım süreçlerini hızlandırır.
- **Hata Azaltma**: Manuel yapılandırma hatalarını en aza indirir. Herhangi bir hata durumunda, IaC dosyaları ile eski bir yapılandırmaya hızlıca geri dönülebilir.
- **Yeniden Kullanılabilirlik**: Aynı kodla farklı ortamlarda aynı altyapı hızlıca yeniden oluşturulabilir. Bu, tutarlılığı artırır ve konfigürasyon hatalarını azaltır.
- **Ölçeklenebilirlik**: Altyapı kaynaklarını hızlıca ölçeklendirme ve yönetme imkanı sağlar.

### IaC'nin DevOps'taki Rolü
- **DevOps Entegrasyonu**: IaC, DevOps süreçlerinin bir parçası olarak kullanılır ve CI/CD hatlarına entegre edilir. Bu, yazılımın geliştirme ve dağıtım süreçlerinde altyapı değişikliklerinin otomatik olarak yapılmasını sağlar.
- **Hızlı ve Tutarlı Ortamlar**: Geliştirme, test ve üretim ortamları arasında tutarlılığı sağlar ve bu ortamların hızlıca oluşturulmasına olanak tanır.

### IaC Araçları
- **Ansible**: Konfigürasyon yönetimi ve uygulama dağıtımı için kullanılır.
- **Puppet**: Otomasyon için güçlü bir araçtır.
- **Chef**: Sunucu yapılandırma ve uygulama dağıtımı için kullanılır.
- **Terraform**: Çoklu bulut platformlarında altyapıyı yönetmek için kullanılır.
- **AWS CloudFormation**: AWS'deki kaynakları yönetmek için kullanılır.
- **Google Cloud Deployment Manager**: Google Cloud Platform kaynaklarını yönetmek için kullanılır.
- **Azure Resource Manager**: Microsoft Azure kaynaklarını yönetmek için kullanılır.
- **Vagrant**: Geliştirme ortamları oluşturmak için kullanılır.
- **Pulumi**: Altyapıyı kod olarak yönetmek için modern bir araçtır.
- **env0**: Altyapı otomasyonunu yönetmek için kullanılır.

## Ansible Nedir?
- **Ansible**: Ansible, açık kaynaklı bir otomasyon aracıdır ve konfigürasyon yönetimi, uygulama dağıtımı, görev otomasyonu gibi işlemler için kullanılır. Ansible, basit ama güçlü bir otomasyon aracı olarak bilinir ve YAML dili kullanılarak yapılandırma dosyaları yazılır.

---
# 8. Gün - EC2 ve Güvenlik Grupları

Staj programımızın sekizinci gününde Amazon Web Services (AWS) EC2 (Elastic Compute Cloud) ve Güvenlik Grupları konularını inceledik. EC2, bulut bilişimde altyapı olarak hizmet (IaaS) sağlayan temel bileşenlerden biridir.

## EC2 Nedir?
- **EC2 (Elastic Compute Cloud)**: AWS tarafından sağlanan ve bulut üzerinde sanal makineler çalıştırmaya olanak tanıyan bir hizmettir. EC2, esnek bir şekilde ölçeklenebilirliği ve yüksek erişilebilirliği ile bilinir.
- **EC2'nin Sağladığı Hizmetler**:
  - **Sanal Makine Kiralama (EC2)**: Sanal makineler oluşturmak ve çalıştırmak.
  - **Veri Depolama (EBS)**: Sanal sürücüler üzerinde veri depolamak.
  - **Yük Dengeleme (ELB)**: Yükü sanal makineler arasında dağıtmak.
  - **Otomatik Ölçekleme (ASG)**: Hizmetlerin artan veya azalan taleplere göre otomatik olarak ölçeklenmesi.

### EC2 Boyutlandırma ve Konfigürasyon İşlemleri
- **İşletim Sistemleri**: Linux, Windows, MacOS.
- **İşlemci Gücü**: Makinenin ne kadar işlem gücüne ihtiyaç duyduğunu belirlemek (CPU).
- **Bellek Gereksinimleri**: Ne kadar RAM gerektiğini belirlemek (RAM).
- **Depolama Alanı Gereksinimleri**:
  - **Ağa Bağlı Depolama (EBS&EFS)**.
  - **Donanım Tabanlı (EC2 instance store)**.
- **Ağ Kartı**: Kart hızı, Public IP adresi.
- **Güvenlik Duvarı Kuralları (Security Groups)**: Giden ve gelen trafiği kontrol etmek.
- **Bootstrap Script (EC2 User Data)**: Makine başlatılırken özel komutlar çalıştırmak.

### EC2 User Data
- **EC2 User Data**: EC2 User Data kullanarak, makineleri oluştururken belirli koşullara veya uygulamalara göre özelleştirebiliriz. Bu, "bootstrapping" olarak bilinir ve makine ilk başlatıldığında bir kez çalıştırılır. Örnek görevler:
  - Güncellemelerin yüklenmesi.
  - Yazılım veya uygulamaların kurulması.
  - İnternetten ilgili paketlerin indirilmesi.

### EC2 Instance Türleri
- **Genel Amaçlı (General Purpose)**: Genel iş yetenekleri için uygun, dengelemeli işlem gücü, bellek ve ağ kapasitesi sunar.
- **İşlem Optimizasyonu (Compute Optimized)**: Güçlü işlemcilere ihtiyaç duyan uygulamalar için idealdir.
- **Bellek Optimizasyonu (Memory Optimized)**: Yüksek veri bloklarını işleyen uygulamalar için uygundur.
- **Depolama Optimizasyonu (Storage Optimized)**: Yüksek sıralı okuma ve yazma işlemleri gerektiren büyük veri kümeleri için idealdir.

## Güvenlik Grupları (Security Groups)
- **Güvenlik Grupları**: AWS'de ağ güvenliğinin temelini oluşturur. Güvenlik grupları, EC2 instance'larına gelen ve giden trafiği kontrol eder.
  - **Inbound Traffic (Gelen Trafik)**: Instance'a gelen trafiği kontrol eder.
  - **Outbound Traffic (Giden Trafik)**: Instance'tan dışarıya giden trafiği kontrol eder.
  - **Varsayılan Kurallar**:
    - **Inbound**: Varsayılan olarak tüm gelen trafik engellenir.
    - **Outbound**: Varsayılan olarak tüm giden trafik izinlidir.

### Güvenlik Grubu Özellikleri
- **Birden Fazla Instance Kullanımı**: Bir güvenlik grubu birden fazla instance tarafından kullanılabilir.
- **Bölge ve VPC'ye Göre Çalışma**: Güvenlik grupları, tanımlandıkları bölge ve VPC ile sınırlıdır.
- **Aktif Olarak Çalışma**: Güvenlik grupları, EC2 instance'larının dışında çalışır, bu nedenle eğer trafik bir şekilde engellenirse, EC2 instance bunu göremez.
- **SSH İzni**: SSH izni için ayrı bir güvenlik grubu tanımlamak önerilir.

### Klasik Portlar
- **SSH (22)**: Linux instance'larına bağlanmak için kullanılır.
- **FTP (21)**: Dosya paylaşımına dosya yüklemek için kullanılır.
- **SFTP (22)**: SSH kullanarak dosya yükleme.
- **HTTP (80)**: Güvenli olmayan web sitelerine erişim.
- **HTTPS (443)**: Güvenli web sitelerine erişim.
- **RDP (3389)**: Windows instance'larına bağlanmak için kullanılır.

### SSH Kullanımı
- **SSH Kullanımı**: SSH, uzak bir makineye terminal üzerinden bağlanmamızı ve onu kontrol etmemizi sağlar.

## EC2 Satın Alma Seçenekleri
- **On Demand Instances**: Kısa süreli iş yükleri ve tahmin edilebilir fiyatlandırma için kullanılır.
- **Reserved Instances**: Uzun süreli iş yükleri için idealdir. 1 yıl veya 3 yıl gibi rezervasyon dönemleri ile maliyet avantajı sağlar.
- **Spot Instances**: Kısa süreli iş yükleri için düşük maliyetlidir, ancak bu instance'ları kaybetme riski vardır.
- **Dedicated Hosts**: Fiziksel bir sunucuyu kiralayarak, tüm kullanım haklarını elinde bulundurma imkanı verir.

### EC2 Instance Satın Alma Modelleri
- **On-Demand**: Anlık ihtiyaçlara yönelik kiralama, en yüksek maliyetli ancak en esnek seçenektir.
- **Reserved Instances**: Daha uzun süreli kiralama ile %75'e varan indirim sağlar.
- **Spot Instances**: Maliyet etkinliği en yüksek olan modeldir, ancak kritik iş yükleri için uygun değildir.

---

# 9. Gün - ELK Stack

Staj programımızın dokuzuncu gününde ELK Stack (Elasticsearch, Logstash, Kibana) üzerine yoğunlaştık. ELK Stack, veri toplama, işleme, arama, analiz ve görselleştirme işlemleri için kullanılan popüler bir açık kaynak araç setidir.

## ELK Stack Nedir?
- **ELK Stack**: Elastic tarafından geliştirilmiş, kullanıcıların herhangi bir kaynaktan gelen veriyi gerçek zamanlı olarak aramasını, analiz etmesini ve görselleştirmesini sağlayan açık kaynaklı bir ürün grubudur. ELK Stack üç ana bileşenden oluşur: Elasticsearch, Logstash ve Kibana.

### ELK Stack Bileşenleri
1. **Elasticsearch**: Dağıtık, RESTful arama ve analiz motorudur. Elasticsearch, büyük veri kümeleri üzerinde hızlı arama ve veri analizi yapar. Apache Lucene üzerine inşa edilmiştir ve log analitiği, tam metin arama, güvenlik istihbaratı ve iş zekası gibi kullanımlar için yaygın olarak tercih edilir.
2. **Logstash**: Sunucu tarafında çalışan açık kaynaklı veri işleme aracı. Logstash, veri toplayıp, işleyip ve belirli hedeflere gönderir. Elasticsearch ile entegre çalışarak verilerin toplanmasını ve indekslenmesini sağlar.
3. **Kibana**: Elasticsearch tarafından toplanan ve işlenen verilerin görselleştirilmesini sağlayan bir araçtır. Veri görselleştirme, izleme ve analiz işlemleri için kullanıcı dostu bir arayüz sunar.

## Elasticsearch
### Elasticsearch Nedir?
- **Elasticsearch**: 2010 yılında piyasaya sürülen ve Apache Lucene üzerine inşa edilen dağıtık bir arama ve analiz motorudur. Elasticsearch, log analitiği, tam metin arama, güvenlik istihbaratı, iş analitiği ve operasyonel zeka gibi birçok kullanım durumunda tercih edilir.

### Elasticsearch'ü Kimler Kullanıyor?
- **Kullanıcılar**: Uber, Udemy, Slack, Netflix, Medium ve LinkedIn gibi birçok büyük şirket Elasticsearch'ü sistemlerinde kullanmaktadır.

### Elasticsearch Kurulumu
- **RPM ve Docker Kurulumu**:
  - RPM paketleri ile kurulum için, Elasticsearch imza anahtarı makineye eklenir, ardından gerekli paketler kurulur.
  - Docker üzerinde kurulumda, Elasticsearch imajı çekilir ve tek bir düğüm olarak çalıştırılır. Multi-node konfigürasyonu için `docker-compose.yml` dosyası kullanılır.

### Elasticsearch Özellikleri
- **Avantajlar**:
  - Gerçek zamanlı arama motoru.
  - Kolay ölçeklenebilirlik ve dağıtık yapı.
  - Java tabanlı olduğu için tüm platformlarda çalışabilir.
  - Açık kaynak kodlu ve ücretsizdir.
- **Dezavantajlar**:
  - Büyük veri kümeleri üzerinde çalışırken sınırlamalar olabilir.
  - Öğrenme eğrisi mevcuttur ve bazı işletme çözümleri için kullanımı karmaşık olabilir.

### Elasticsearch Temel Kavramları
- **Node**: Bir Elasticsearch örneğini temsil eder. Bir kümedeki her bir Elasticsearch örneği bir "node" olarak adlandırılır.
- **Cluster**: Birden fazla nodun bir araya gelerek oluşturduğu küme. Kümeler, tüm verilerin tek bir indeks altında birleşmesini sağlar.
- **Document**: JSON formatında depolanan veri birimidir. Her belge, benzersiz bir kimlik ile ilişkilendirilir.
- **Index**: Belgelerin toplandığı yapı. Bir ilişkisel veritabanında tabloya karşılık gelir.
- **Shard**: Bir indeksin parçalara bölünerek depolanmasıdır. Veriler büyük miktarda olduğunda, indeksler shard'lara bölünür ve farklı düğümlerde saklanır.
- **Replica**: Shard'ların yedek kopyalarıdır. Veri kaybını önlemek ve arama performansını artırmak için kullanılır.

### Elasticsearch Mimarisi
- **Cluster Mimarisi**: Elasticsearch, bir küme mimarisi üzerine kurulmuştur. Her bir düğüm, kümenin bir parçasıdır ve tüm düğümler birbirleriyle iletişim halindedir. Kümedeki bir düğüm, "master node" olarak atanabilir ve bu düğüm kümenin genel durumunu yönetir.

## Logstash
### Logstash Nedir?
- **Logstash**: ELK Stack'in veri toplama ve işleme bileşenidir. Farklı veri kaynaklarından gelen verileri toplar, filtreler ve Elasticsearch'e veya diğer hedeflere gönderir. Logstash, çeşitli veri kaynaklarını destekleyen 200'den fazla eklenti ile uyumludur.

### Logstash Kurulumu
- **Debian ve CentOS Üzerinde Kurulum**:
  - Debian tabanlı sistemlerde, gerekli anahtar ve depo tanımlamaları yapıldıktan sonra Logstash yüklenir.
  - CentOS üzerinde benzer adımlarla Public Signing Key eklenir ve depo tanımlamaları yapılarak Logstash yüklenir.

### Beats Nedir?
- **Beats**: Veri toplamak için kullanılan hafif veri göndericileridir. Filebeat, Metricbeat, Packetbeat gibi farklı Beats türleri, farklı veri tiplerini toplamak için kullanılır. Beats, verileri doğrudan Elasticsearch'e veya Logstash'e gönderir.

## Kibana
### Kibana Nedir?
- **Kibana**: ELK Stack'in veri görselleştirme aracıdır. Elasticsearch ile entegre çalışarak verilerin görsel olarak analiz edilmesini sağlar. Kullanıcı dostu arayüzü ile zaman analizi, uygulama izleme ve raporlama gibi işlemler için kullanılır.

### Kibana Özellikleri
- **Özellikler**:
  - Farklı görselleştirme seçenekleri: Histogram, pasta grafiği, çizgi grafiği, ısı haritası vb.
  - Verilerin indekslenmesi ve tablo tarzı yapılar oluşturulması.
  - Tamamen özelleştirilebilir kullanıcı arayüzü.
- **Kurulum**:
  - Kibana, Elasticsearch ve Logstash gibi diğer bileşenler gibi kurulabilir. Yum repo tanımlamaları yapıldıktan sonra kurulum tamamlanır.

### Dashboard Yönetimi ve Görselleştirme
- **Dashboard Yönetimi**: Kibana'da, belirli bir indeks desenine (index pattern) dayalı olarak farklı tablolar veya histogramlar oluşturulabilir. Bu görselleştirmeler birleştirilerek dashboard oluşturulabilir. Hem görselleştirmeler hem de dashboard'lar tamamen özelleştirilebilir.



---


# 10. Gün - Mesajlaşma Sıra Yönetimi ve Mesaj Brokerları

Staj programımızın onuncu gününde dağıtık sistemlerde mesajlaşma sırası yönetimi ve mesaj brokerlarının temel kavramlarını inceledik. Bu konular, özellikle büyük ölçekli sistemlerde bileşenlerin birbiriyle verimli bir şekilde iletişim kurmasını sağlamak için kritik öneme sahiptir.

## Giriş - İletişimin Önemi
- **Dağıtık Sistemler**: Birden fazla bileşenin (düğüm) birbirleriyle etkileşim kurup bilgi paylaşması gereken sistemlerdir. Bu tür sistemlerde etkili iletişim ve koordinasyon, sistemin sorunsuz çalışması ve yüksek hata toleransı için hayati önem taşır.
- **Mesaj Brokerları**: Bileşenler arasında güvenilir ve asenkron iletişim sağlayan köprü görevi görürler. Mesaj brokerları, gönderen ve alıcılar arasında merkezi bir mimari sunar.

## Mesaj Brokerlarını Anlama
- **Mesaj Brokerlarının İşlevi**: Mesajları doğrulama, saklama, yönlendirme ve gerekli hedeflere teslim etme işlevlerini yerine getirirler. Mesaj brokerları, gönderen ve alıcıların aynı platformda veya aynı dilde yazılmasına gerek kalmadan çalışabilmelerini sağlar.

## Bileşenler
- **Kuyruk (Queue)**: Mesaj brokerlarının mesajları sakladığı veri türüdür. FIFO (First In, First Out) mantığıyla çalışır.
- **Exchange**: Mesajları doğru kuyruğa ve alıcıya yönlendiren bileşendir. Anahtar değerler kullanılarak mesajlar ve kuyruklar eşleştirilir.
- **Tüketici (Consumer/Subscriber)**: Mesaj brokerından veri talep eden ve tüketen uç noktadır. Veriyi aldıktan sonra onay mesajı gönderir.
- **Üretici (Producer/Publisher)**: Mesaj brokerına mesaj veya veri gönderen uç noktadır.

## Kuyruklar
- **Kuyrukların İşlevi**: Mesajların doğru sırayla alınmasını ve aynı sırayla alıcıya iletilmesini sağlar. Ağ sorunları gibi durumlarda mesajlar yeniden sıraya alınır.
- **FIFO**: İlk giren ilk çıkar mantığı ile çalışır, bu da sistemin asenkron çalışmasına izin verir.

## Exchange Türleri
- **Direct Exchange**: Bir yönlendirme anahtarı kullanarak mesajları doğru kuyruğa iletir. Yönlendirme anahtarı, mesajın içeriği veya amacı hakkında bilgi taşır.
- **Fanout Exchange**: Yönlendirme anahtarına ihtiyaç duymaz, mesajları tüm tüketicilere iletir. Genellikle toplu duyurular veya gerçek zamanlı yayınlar için kullanılır.
- **Topic Exchange**: Belirli bir konuda birden fazla kuyruk için yönlendirme anahtarları kullanılır. Örneğin, bir konuya ilgi duyan tüm tüketiciler bu konudaki mesajları alır.

## Mesaj Türleri
- **Olay (Event)**: Tüm uygulamalara bir olayın meydana geldiğini bildiren mesajlardır. Örneğin, bir mesaj alındığında göndericiye geri bildirim gönderilir.
- **Komut (Command)**: Alıcıdan bir isteği yerine getirmesini talep eden mesajlardır. Genellikle direct exchange ile iletilir.

## Mesaj Broking Desenleri
- **Yayın/Abone (Pub/Sub)**: Gönderen, belirli konulara veya kanallara mesaj yayınlar ve bu mesajlar, ilgilenen tüm alıcılara iletilir. Bir mesaj birden fazla alıcıya ulaşır.
- **Noktadan Noktaya (Point-to-Point)**: Bir mesaj, bir göndericiden belirli bir alıcıya (kuyruk) gönderilir ve yalnızca bir alıcı tarafından tüketilir.
- **İstek/Yanıt (Request/Reply)**: Bir bileşen, bir hizmete istek mesajı gönderir ve karşılık olarak bir yanıt mesajı bekler. Bu desen, genellikle Uzaktan Prosedür Çağrısı (RPC) senaryolarında kullanılır.

## Örnek Mesaj Brokerları
### RabbitMQ
- **RabbitMQ**: En popüler, açık kaynaklı mesaj brokerıdır. Çeşitli protokolleri destekler ve tüketici tarafından onaylanana kadar mesajları saklar. 
- **RabbitMQ Desenleri**: RabbitMQ, kuyruk ve yayın/abone yöntemlerini destekler. Ayrıca birden fazla üreticiden gelen aynı tür mesajların tek bir kuyrukta toplanması gibi desenler de desteklenir.

### Kafka
- **Kafka**: Yüksek verimliliğe sahip, açık kaynaklı bir dağıtık akış platformudur. Büyük veri uygulamaları için uygundur ve veri akışlarını yüksek hata toleransı ile yönetir.
- **Kafka Zookeeper**: Kafka'nın bileşenlerinden biri olan Zookeeper, küme koordinasyonunu sağlar, lider seçimlerini gerçekleştirir ve dinamik konu yapılandırmalarını izler.

### Redis
- **Redis**: Bellek içi veri yapısı deposu olarak kullanılabilen hızlı ve verimli bir mesaj brokerıdır. Düşük gecikme süresi ve yüksek throughput sunar, ancak kalıcılığı Kafka veya RabbitMQ kadar sağlam değildir.
- **Redis Desenleri**: Redis, hem Üretici-Tüketici hem de Yayın/Abone desenlerini destekler.

### Mesaj Broker Kullanım Senaryoları
- **RabbitMQ**: Karmaşık iletişim gereksinimleri olan ancak çok yüksek hız gerektirmeyen durumlar için idealdir.
- **Redis**: Gerçek zamanlı uygulamalar için daha uygundur. Kalıcılığın kritik olmadığı durumlarda mükemmel bir seçenektir.
- **Kafka**: Büyük ve kritik veri akışları için daha uygundur. Yüksek hata toleransı ve veri saklama süreleri sunar.



---
# 11. ve 12. Gün - CI/CD Development

Staj programımızın on birinci gününde CI/CD (Continuous Integration/Continuous Deployment) süreçleri üzerine odaklandık. CI/CD, modern yazılım geliştirme süreçlerinin ayrılmaz bir parçası olup, yazılımın daha hızlı, güvenilir ve hatasız bir şekilde teslim edilmesini sağlar.


## CI/CD Nedir?
- **CI/CD**: CI, "Continuous Integration" anlamına gelir ve geliştiricilerin kod değişikliklerini sürekli olarak birleştirip test etmelerini sağlar. CD ise "Continuous Deployment" veya "Continuous Delivery" anlamına gelir ve yazılımın sürekli olarak dağıtılmasını veya teslim edilmesini ifade eder.
- **CI/CD'nin Amacı**: Kod entegrasyonunu, yazılımın inşasını, test edilmesini ve üretim ortamına dağıtılmasını otomatikleştirerek yazılım teslimatını hızlandırmak ve kalitesini artırmaktır.

## CI/CD Nasıl Çalışır?
- **Kod Entegrasyonu**: Geliştirici kodda değişiklik yaptığında, bu değişiklikler merkezi bir depozito’ya (repository) gönderilir. Bu işlem, kodun derlenmesini ve yeni bir binary oluşturulmasını tetikler.
- **Kod Testi**: Yeni binary, doğru çalıştığından emin olmak için test edilir. Bu testler manuel veya otomatik araçlarla gerçekleştirilebilir.
- **Kod Dağıtımı**: Testler başarılı olursa, yeni binary bir sahneleme ortamına dağıtılır. Sahneleme ortamı, üretim ortamına benzer bir test ortamıdır.
- **Kod Tanıtımı**: Sahneleme ortamındaki testler de başarılı olursa, binary üretim ortamına tanıtılır ve kullanıcılara sunulur.

### CI/CD'nin Faydaları
- **Kalite Artışı**: Otomatik test süreçleri sayesinde hatalar erken tespit edilip düzeltilebilir.
- **Hızlı Teslimat**: Otomasyon, yazılım teslimatını hızlandırarak yeni özelliklerin daha hızlı sunulmasını sağlar.
- **Maliyet Azaltımı**: Otomatik süreçler, geliştiricilerin zamanını daha verimli kullanmasını sağlar ve manuel işlemlerin azaltılmasıyla maliyetleri düşürür.

## Continuous Integration (CI)
- **Continuous Integration**: Geliştiricilerin kod değişikliklerini düzenli olarak merkezi bir depoya entegre etmeleri sürecidir. Bu entegrasyon sonrası, kod otomatik olarak derlenir ve test edilir.

### Neden CI'ya İhtiyaç Duyulur?
- **Geçmişteki Zorluklar**: Eskiden, geliştiriciler kodlarını uzun süre izole çalıştıktan sonra ana dal ile birleştirirdi. Bu süreçte kod birleştirmeleri zor ve zaman alıcı olurdu. CI, bu süreci otomatikleştirerek zorlukları ortadan kaldırır.

### CI Nasıl Çalışır?
- **Sürekli Entegrasyon**: Geliştiriciler, kod değişikliklerini sürekli olarak merkezi bir depoya gönderirler. Her gönderim, otomatik olarak derlenir ve birim testleri çalıştırılır. Bu süreç, hataların erken tespit edilmesini sağlar.

### CI'nın Faydaları
- **Geliştirici Verimliliği**: Geliştiricilerin manuel işlerden kurtulmasını sağlar ve daha az hata ile daha hızlı yazılım geliştirmeye olanak tanır.
- **Hızlı Güncellemeler**: Yazılım güncellemelerini daha hızlı ve düzenli bir şekilde müşterilere ulaştırmayı sağlar.

## CI/CD Araçları
### SonarQube
- **SonarQube**: Kod kalitesini sürekli izlemek için kullanılan açık kaynaklı bir platformdur. Statik kod analizi, kod kapsamı analizi ve güvenlik taramaları gibi özellikler sunar.

### Harbor
- **Harbor**: Konteyner imajlarını güvenli, özel ve ölçeklenebilir bir şekilde saklamak ve yönetmek için kullanılan bir konteyner kayıt defteri hizmetidir. Harbor, Docker Registry üzerine kuruludur ve güvenlik, gizlilik ve ölçeklenebilirlik özellikleri sunar.

### Nexus Artifactory
- **Nexus Artifactory**: Yazılım geliştirme ekiplerinin JAR, WAR ve POM gibi yapı artifactlerini depolayıp yönetebileceği merkezi bir depo yöneticisidir. Artefaktların sürümlendirilmesi, aranması ve filtrelenmesi gibi özellikler sunar.

### HashiCorp Vault
- **HashiCorp Vault**: API şifreleme anahtarları, parolalar ve sertifikalar gibi gizli bilgilerin güvenli bir şekilde saklanması ve yönetilmesi için kullanılan kimlik tabanlı bir gizlilik ve şifreleme yönetim sistemidir.

## Jenkins
- **Jenkins**: Java ile yazılmış, açık kaynaklı bir sürekli entegrasyon sunucusudur. Jenkins, yazılım geliştirme yaşam döngüsünün her aşamasını destekler: inşa etme, test etme, belgeleme, dağıtım ve diğer aşamalar.
- **Jenkins Pluginleri**: Jenkins, 1800'den fazla eklenti sunar. Bu eklentiler, Jenkins'in yeteneklerini genişletir ve neredeyse her sürekli entegrasyon ve sürekli dağıtım aracı ile entegre olmasına olanak tanır.
- **Jenkinsfile**: Jenkins pipeline'larını tanımlamak için kullanılan bir metin dosyasıdır. Bu dosya, Groovy, Python veya YAML ile yazılabilir ve aynı depoda saklanabilir.

## GitHub
- **GitHub**: GitHub, Git tabanlı bir kaynak kod yönetim platformudur. Kod depolama, işbirliği, erişim kontrolü ve proje yönetimi gibi birçok özellik sunar.
- **GitHub Actions**: GitHub'ın CI/CD platformudur ve otomatikleştirilmiş iş akışları oluşturmaya olanak tanır.


## GitLab Nedir?

**GitLab**, büyük DevOps ve DevSecOps projeleri için açık kaynaklı bir kod deposu ve işbirlikçi yazılım geliştirme platformudur. GitLab, bireyler için ücretsizdir.

- **GitLab**, çevrimiçi kod depolama, sorun takibi ve CI/CD (Sürekli Entegrasyon/Sürekli Dağıtım) yetenekleri sunar. Depo, farklı geliştirme zincirlerini ve sürümleri barındırma imkanı tanır ve kullanıcıların önceki kodları incelemesine ve beklenmeyen sorunlar durumunda bu kodlara geri dönmesine olanak sağlar.

- **GitLab**, GitHub'ın bir rakibidir. GitHub, Linus Torvalds'ın Linux çekirdeği geliştirme projeleri gibi birçok projeye ev sahipliği yapmaktadır. GitLab, Git tabanlı sürüm kontrol sistemi üzerine inşa edildiği için, kaynak kod yönetimi açısından çok benzer şekilde çalışır.

- **GitLab**, yazılım geliştirme yaşam döngüsünün her aşaması için uçtan uca DevOps yetenekleri sunar. GitLab’ın sürekli entegrasyon (CI) yetenekleri, geliştirme ekiplerinin kodlarını otomatik olarak inşa etmesini ve test etmesini sağlar. Güvenlik yetenekleri, tarama sonuçlarını geliştiricinin kendi CI pipeline'ı veya iş akışı içinde sunar ve güvenlik uzmanları için zafiyet yönetiminde yardımcı olan bir kontrol paneli içerir. Kullanıcılar ayrıca, GitLab'ın Peach Tech ve Fuzzit şirketlerini satın almasıyla sunulan fuzz test etme avantajlarından da yararlanabilirler.


## Planlama (Plan)

GitLab, kullanıcılarına güçlü planlama araçları sunar ve herkesin senkronize olmasını sağlar. Bu araçlar, portföy planlaması ve yönetimi için epikler, gruplar (programlar) ve kilometre taşları gibi bileşenlerle proje ilerlemesini organize etmeye ve takip etmeye olanak tanır. GitLab, Waterfall'dan DevSecOps'a kadar her türlü metodoloji için basit ve esnek bir planlama yaklaşımı sunar. Bu özellikler, küçük ekiplerden büyük işletmelere kadar her boyutta ekibin ihtiyaçlarını karşılar. GitLab, ekiplerin proje çalışmalarını organize etmelerine, planlamalarına, hizalamalarına ve izlemelerine yardımcı olarak, doğru zamanda doğru işlerin yapılmasını sağlar. Ayrıca, fikirden üretime kadar olan süreçte sorunların uçtan uca görünürlüğünü ve izlenebilirliğini sağlar.

- **Team Planning**: Takım planlaması için çeşitli araçlar sunar.
- **Portfolio Management**: Proje yönetimi ve portföy yönetimi sağlar.
- **Requirements Management**: Gereksinim yönetimi özellikleri.
- **Quality Management**: Kalite yönetimi için araçlar içerir.
- **Design Management**: Tasarım süreçlerini yönetir.
- **DORA Metrics**: Yazılım teslim performansını ölçer.
- **Value Stream Management**: Değer akış yönetimi özellikleri.
- **DevOps Reports**: DevOps raporları sunar.
- **Wiki**: Projeler için wiki sayfaları oluşturma imkanı.
- **Pages**: Projeler için web sayfaları oluşturma imkanı.

## Kod Yazma ve Yönetme (Create)

GitLab, kod yazma, görüntüleme ve yönetme süreçlerini güçlü dallanma araçları ile destekler. Bu sayede ekipler, projeleri için kodu kolayca organize edebilir ve yönetebilir. GitLab, epikler, gruplar ve kilometre taşları ile portföy planlaması ve yönetimini sağlar. Her ne kadar süreçleriniz Waterfall veya DevSecOps metodolojisine dayanıyor olsa da, GitLab'ın esnek ve basit planlama yaklaşımı, küçük ekiplerden büyük işletmelere kadar herkesin ihtiyaçlarını karşılar. Bu sayede, ekiplerin doğru zamanlarda doğru işler üzerinde çalışması ve fikirden üretime kadar tüm yaşam döngüsü boyunca işlerin uçtan uca izlenebilirliği sağlanır.

- **Source Code Management**: Kaynak kod yönetimi sağlar.
- **Code Review Workflow**: Kod gözden geçirme iş akışları sunar.
- **Web IDE**: Tarayıcı üzerinden kullanılabilen bir geliştirme ortamı sağlar.
- **GitLab CLI**: Komut satırı üzerinden GitLab ile etkileşim.
- **Remote Development**: Uzaktan geliştirme imkanı sunar.

## Doğrulama (Verify)

GitLab, üretim kodu için sıkı kalite standartlarını otomatik testler ve raporlamalar ile sağlar. Bu süreçte, sürekli entegrasyon (CI) ile kodların derlenmesi, entegrasyonu ve doğrulanması otomatikleştirilir. GitLab'ın endüstri lideri CI yetenekleri, otomatik testler, Statik Uygulama Güvenlik Testi (SAST), Dinamik Uygulama Güvenlik Testi (DAST) ve kod kalitesi analizi sunarak geliştiricilere ve testçilere kodlarının kalitesi hakkında hızlı geri bildirim sağlar. Paralel yürütmeyi ve eşzamanlı testleri destekleyen pipeline'lar ile ekipler, her commit hakkında hızlıca içgörü kazanarak daha yüksek kalitede kodları daha hızlı bir şekilde teslim eder.

- **Continuous Integration (CI)**: Sürekli entegrasyon imkanı.
- **Pipeline Composition**: Pipeline bileşenlerini oluşturma.
- **Secrets Management**: Gizli bilgilerin yönetimi.
- **GitLab Runner Core & SaaS**: GitLab Runner kullanarak işlemlerinizi yürütün.
- **Runner Fleet**: Farklı makinelerde çalışan runner'ları yönetin.
- **Code Testing and Coverage**: Kod testi ve kapsam analizi.
- **Build Artifacts**: Yapı artefaktlarını yönetin.
- **Merge Trains**: Merge işlemlerini yönetin.
- **Review Apps**: İnceleme için uygulama dağıtımı yapın.

## Paketleme (Package)

GitLab, uygulamaların ve bağımlılıkların paketlenmesi, konteynerlerin ve yapı artefaktlarının yönetimi için gerekli araçları sunar. GitLab, dahili olarak yapılandırılmış ve güvenli bir paket kayıt defteri ve konteyner kayıt defteri sunar. Bu kayıt defterleri, GitLab kaynak kodu yönetimi ve CI/CD pipeline'ları ile sorunsuz bir şekilde entegre çalışır. DevSecOps hızlandırmasını sağlamak ve yazılımın pazara daha hızlı ulaşmasını temin etmek için otomatikleştirilmiş yazılım pipeline'ları, kesintisiz bir şekilde çalışır.

- **Package Registry**: Paket kayıt defteri.
- **Container Registry**: Konteyner kayıt defteri.
- **Helm Chart Registry**: Helm Chart kayıt defteri.
- **Dependency Proxy**: Bağımlılık proxy hizmeti.

## Güvenlik (Secure)

GitLab, yazılım geliştirme yaşam döngüsüne entegre edilmiş güvenlik yetenekleri sunar. Bu özellikler arasında Statik Uygulama Güvenlik Testi (SAST), Dinamik Uygulama Güvenlik Testi (DAST), Konteyner Tarama ve Bağımlılık Tarama yer alır. Bu özellikler, güvenli uygulamaların teslim edilmesine yardımcı olur ve lisans uyumluluğunu sağlar.

- **SAST**: Statik Uygulama Güvenliği Testi.
- **Secret Detection**: Gizli bilgilerin tespiti.
- **Code Quality**: Kod kalitesini ölçme araçları.
- **DAST**: Dinamik Uygulama Güvenliği Testi.
- **API Security**: API güvenliği.
- **Fuzz Testing**: Fuzz testi.
- **Software Composition Analysis**: Yazılım bileşimi analizi.
- **Container Scanning**: Konteyner taraması.
- **GitLab Advisory Database**: GitLab danışmanlık veritabanı.

## Dağıtım (Deploy)

GitLab'ın entegre sürekli dağıtım (CD) çözümü, bir veya binlerce sunucuda kodu sıfır dokunuşla dağıtmanıza olanak tanır. GitLab, uygulamaların sürüm ve dağıtımını otomatikleştirerek teslimat döngüsünü kısaltır, manuel süreçleri düzenler ve ekip hızını artırır. Sıfır dokunuşlu sürekli teslimat (CD) doğrudan pipeline'a entegre edilmiştir, bu da dağıtımların sahneleme ve üretim gibi birçok ortama otomatik olarak yapılabileceği anlamına gelir. Sistem, ileri düzey desenler için bile ne yapacağını bilir - örneğin, kanarya dağıtımları için. Özellik bayrakları, dahili denetim/izlenebilirlik ve isteğe bağlı ortamlar sayesinde, her zamankinden daha hızlı ve daha güvenle teslimat yapabilirsiniz.

- **Continuous Delivery**: Sürekli teslimat.
- **Feature Flags**: Özellik bayrakları.
- **Release Orchestration**: Sürüm orkestrasyonu.
- **Environment Management**: Ortam yönetimi.
- **Auto DevOps**: Otomatik DevOps.
- **Deployment Management**: Dağıtım yönetimi.
- **Infrastructure as Code**: Kod olarak altyapı yönetimi.

## İzleme (Monitor)

GitLab, olayların ciddiyetini ve sıklığını azaltmanıza yardımcı olacak geri bildirim ve araçlar sunar. Bu sayede yazılımı sık sık ve güvenle yayınlayabilirsiniz.

- **Incident Management**: Olay yönetimi.
- **On-call Schedule Management**: Nöbet yönetimi.
- **Error Tracking**: Hata takibi.
- **Service Desk**: Hizmet masası özellikleri.

## Yönetim (Govern)

GitLab, kullanıcıların güvenlik açıklarını, politikalarını ve uyumluluk süreçlerini yönetmelerine yardımcı olur. Bu sayede, organizasyon genelinde güvenlik açıkları, politikaları ve uyumluluk yönetimi sağlanır.

- **Audit Events**: Denetim olayları.
- **Compliance Management**: Uyum yönetimi.
- **Security Policy Management**: Güvenlik politikası yönetimi.
- **Vulnerability Management**: Zafiyet yönetimi.
- **Dependency Management**: Bağımlılık yönetimi.
- **Release Evidence**: Sürüm kanıtları.
# GitLab Pipelines

GitLab Pipelines, yazılım projelerinin Sürekli Entegrasyon (CI) ve Sürekli Dağıtım (CD) süreçlerini otomatikleştirmek için kullanılan bir araçtır. CI/CD, yazılımın sürekli olarak test edilmesi, inşa edilmesi ve dağıtılmasını ifade eder. GitLab Pipelines, bu süreçleri adımlara ayırır ve yazılım geliştirme sürecini daha hızlı ve verimli hale getirmek için otomatikleştirir.

GitLab Pipelines, GitLab içinde tanımlanmış ve yürütülen otomatikleştirilmiş süreçlerdir. Pipelines, bir YAML dosyası kullanılarak tanımlanır ve birden fazla adımdan oluşur. Her adım, belirli bir işlemi gerçekleştiren bir komut, derleme süreci, test çalıştırması veya dağıtım adımı olabilir. Pipelines, sıralı veya paralel olarak çalıştırılabilecek bir dizi adımı temsil eden bir iş akışı oluşturur.

## Pipelines'in Çalışma Şekli
Pipelines, bir projede yapılan değişikliklerle otomatik olarak tetiklenebilir ve farklı dallar (branches) ve versiyonlar üzerinde çalıştırılabilir. Her değişiklik için bir pipeline oluşturulabilir ve kodun test edilmesi, birleştirilmesi, inşa edilmesi ve dağıtılması gibi işlemler otomatikleştirilebilir.

GitLab Pipelines, geliştiricilere yazılım geliştirme sürecini otomatikleştirme, hataları hızlıca tespit etme ve projelerin sürekli olarak güncel ve işlevsel kalmasını sağlama yeteneği sunar. Böylece, yazılım geliştirme süreci hızlanır ve manuel hata olasılığı azaltılır.

GitLab Pipelines ile projelerde sürekli entegrasyon ve dağıtım süreçlerini otomatikleştirerek yazılım geliştirme sürecinin her aşamasında yüksek kalite ve verimlilik sağlanır.

---

# 13. Gün - Kubernetes ve Helm

Staj programımızın on üçüncü gününde Kubernetes ve Helm üzerine yoğunlaştık. Kubernetes, konteynerleştirilmiş uygulamaların yönetimi için açık kaynaklı bir platform olup, Helm ise Kubernetes uygulamalarını yönetmek için kullanılan bir paket yöneticisidir.

## Kubernetes Nedir?
- **Kubernetes**: Kubernetes, taşınabilir, genişletilebilir ve açık kaynaklı bir platformdur. Konteynerleştirilmiş iş yüklerini ve hizmetleri yönetmek için kullanılır ve hem deklaratif yapılandırmayı hem de otomasyonu kolaylaştırır. 2014 yılında Google tarafından tasarlanmış ve açık kaynak topluluğu tarafından desteklenmektedir.
  - **Kullanım Senaryoları**:
    - **Mikroservis Mimarileri**: Uygulamaları bağımsız bileşenler olarak yönetmeyi sağlar.
    - **Sürekli Entegrasyon ve Sürekli Dağıtım (CI/CD)**: Uygulama geliştirme ve dağıtım süreçlerini otomatikleştirir.
    - **Büyük Veri İşleme**: Büyük veri uygulamalarını ölçeklenebilir bir şekilde çalıştırır.
    - **Makine Öğrenimi**: Model eğitimi ve dağıtım süreçlerini hızlandırır.

## Neden Kubernetes Kullanılır?
- **Kubernetes, DevOps senaryolarında yaygın olarak kullanılır** çünkü:
  - **Otomatik Yük Dengeleme**: Uygulama yükünü otomatik olarak dengeler ve trafiği yönetir.
  - **Ölçeklenebilirlik**: Tek bir komutla veya otomatik olarak uygulama ölçeklendirmesi sağlar.
  - **Sağlık Kontrolleri**: Başarısız olan konteynerleri yeniden başlatır, düğümlerdeki sorunları tanımlar ve yeniden planlama yapar.
  - **Orkestrasyon ve Yönetim**: Yerel depolama, genel bulut sağlayıcıları veya ağ depolama çözümleri kullanarak depolama kaynaklarını yönetir.

## Kubernetes Mimarisi
### Ana Bileşenler – Küme Yapısı
- **Küme**: Kubernetes kümesi, uygulamaların çalıştırıldığı bir dizi düğümden oluşan bir ortamdır. Küme, hem uygulama konteynerlerini hem de bu konteynerlerin yönetimini sağlar.
- **Düğüm**: Kubernetes düğümü, konteynerleştirilmiş uygulamaların çalıştırıldığı fiziksel veya sanal bir makinedir. Bir Kubernetes kümesi, bir veya daha fazla düğümden oluşabilir.

### Ana Düğüm – API Sunucusu
- **API Sunucusu**: Kümeler arasındaki bileşenlerin iletişim kurmasını sağlayan merkezi yönetim noktasıdır. Tüm CRUD (Oluşturma, Okuma, Güncelleme, Silme) işlemleri ve kontrol düzlemi istekleri bu sunucu üzerinden gerçekleştirilir.
  - **Görevleri**:
    - API isteklerini doğrulamak ve yetkilendirmek.
    - Etcd ile iletişim kurarak kümenin durum bilgilerini depolamak ve geri almak.
    - Diğer ana bileşenlerle ve işçi düğümlerdeki kubelet bileşenleriyle iletişim kurmak.

### Ana Düğüm – Zamanlayıcı
- **Zamanlayıcı**: Yeni oluşturulan pod'ları Kubernetes kümesindeki uygun işçi düğümlerine atamaktan sorumludur. Zamanlayıcı, kaynakların verimli kullanılmasını sağlamak ve pod'ların doğru çalışmasını temin etmek için çeşitli kriterlere göre düğümleri seçer.
  - **Görevleri**:
    - Yeni pod'ları mevcut işçi düğümleri arasında dağıtmak.
    - CPU, bellek ve diğer kaynakları göz önünde bulundurarak en uygun düğümü seçmek.
    - Düğüm etiketleri, düğüm seçiciler, pod bağımlılığı gibi politikaları dikkate almak.

### Ana Düğüm – Controller Manager
- **Controller Manager**: Kubernetes kümesinde çeşitli kontrol döngülerini (kontrolleri) çalıştıran ve yönetim görevlerini yerine getiren bileşendir. Her kontrol döngüsü, kümenin istenilen durumda olmasını sağlamak için belirli bir kaynağı izler ve yönetir.
  - **Görevleri**:
    - Kontrol döngülerini çalıştırarak kaynakların istenilen durumda olmasını sağlamak.
    - Kullanıcıların ihtiyaçlarına göre kendi kontrol döngülerini oluşturup yönetmelerine olanak tanımak.

### Ana Düğüm – etcd
- **etcd**: Kubernetes kümesinin durum bilgisini tutan dağıtık bir anahtar-değer deposudur. Yüksek erişilebilirlik ve tutarlılık sağlayarak kümenin kalbinde yer alır.
  - **Görevleri**:
    - Küme durum bilgilerini ve yapılandırma verilerini depolamak.
    - Kümedeki herhangi bir düğüm arızalandığında bile verilerin kaybolmamasını sağlamak.

### İşçi Düğüm – Kubelet
- **Kubelet**: Kubernetes işçi düğümlerinde çalışan ve bu düğümlerdeki pod'ları ve konteynerleri yöneten ajan yazılımıdır. Kubelet, her işçi düğümünün kalbidir ve Kubernetes ana düğümleri tarafından belirlenen istenen durumda kalmalarını sağlar.
  - **Görevleri**:
    - Her işçi düğümünde çalışarak pod'ları başlatmak, izlemek ve gerektiğinde durdurmak.
    - Düğümün sağlık durumunu ve kaynak kullanımını izlemek.
    - Kubelet, konteyner çalışma zamanıyla (Docker, CRI-O vb.) etkileşime geçerek konteynerleri başlatır ve yönetir.

### Kubernetes Nesneleri
- **Pod'lar**: Kubernetes'te çalışmanın en küçük ve temel birimi olup, birlikte çalışan bir veya daha fazla konteynerden oluşur.
- **Deployment'lar**: Uygulamanın birden fazla kopyasını (replikasını) kontrol eden, güncelleyen ve yöneten nesnelerdir.
- **ReplicaSets**: Belirli bir sayıda pod'un her zaman çalışır durumda olmasını sağlamak için kullanılan nesnelerdir.
- **Horizontal Pod Autoscaler (HPA)**: Bir uygulamanın yük durumuna göre pod sayısını otomatik olarak ölçeklendiren nesnedir.
- **Service'ler**: Pod'lar arasındaki iletişimi sağlayan ve yaşam döngüsünden bağımsız çalışan nesnelerdir.
- **PersistentVolume (PV) / PersistentVolumeClaim (PVC)**: Pod'lar için kalıcı depolama sağlayan nesnelerdir.
- **Secrets**: Hassas bilgileri (ör. şifreler, OAuth tokenları) güvenli bir şekilde depolamak ve yönetmek için kullanılan nesnelerdir.
- **ConfigMap**: Uygulama yapılandırmalarını depolayan ve bu bilgileri pod'lara sağlayan nesnedir.
- **Ingress**: Tek bir giriş noktasından birden fazla servise erişimi yöneten ve talepleri kümedeki uygun servislere yönlendiren nesnedir.

## Helm Nedir?
- **Helm**: Kubernetes uygulamalarını tanımlamak, kurmak ve yönetmek için kullanılan bir paket yöneticisidir. Helm, uygulamaların manifest dosyalarını standart hale getirir ve bu dosyaların yönetimini kolaylaştırır.
  - **Helm Chart**: Bir uygulamanın Kubernetes manifest dosyalarını içeren bir pakettir. Helm Chart'lar, Helm Depolarında depolanır ve gerektiğinde kullanılabilir.
  - **Helm Release**: Bu paketin (Chart) bir küme üzerinde kurulmasıyla oluşan adımdır.

### Helm'in Faydaları
- **Kolay Kurulum ve Güncelleme**: Tek bir komutla uygulamaları kurma, kaldırma, güncelleme veya geri alma imkanı sağlar.
- **Yapılandırma Yönetimi**: Chart'taki değerleri değiştirerek yapılandırmaları özelleştirme imkanı sunar.
- **Verimli Paketleme ve Dağıtım**: Uygulamalarınızı paketleyebilir ve bir depoya yükleyerek dağıtım yapabilirsiniz.

### Helm Komutları
- **Chart Yönetimi**: `helm create <chart-name>`, `helm package <chart-directory>`, `helm push <chart-package>.tgz <repository-name>` gibi komutlarla Chart'lar oluşturulabilir ve yönetilebilir.
- **Release Yönetimi**: `helm install <release-name> <chart-name>`, `helm upgrade <release-name> <chart-name>`, `helm rollback <release-name> <revision>` gibi komutlarla Chart'ların sürümleri yönetilebilir.

---
# 14. Gün - Terraform

Staj programımızın on dördüncü gününde Terraform üzerine yoğunlaştık. Terraform, HashiCorp tarafından geliştirilen bir Infrastructure as Code (IaC) aracıdır. Bu sunumda, Terraform'un ne olduğunu, nasıl çalıştığını, neden tercih edildiğini, temel terimlerini ve uygulama örneklerini detaylı bir şekilde ele aldık.

## Terraform Nedir?
- **Terraform**, hem bulut hem de yerel altyapı kaynaklarını tanımlamanıza, versiyonlamanıza ve yönetmenize olanak tanıyan bir Infrastructure as Code (IaC) aracıdır. Terraform, insan tarafından okunabilir konfigürasyon dosyalarını kullanarak tüm altyapınızı tek bir akışta yönetmenizi sağlar. Bu, hesaplama kaynakları, depolama ve ağ gibi düşük seviyeli bileşenlerden DNS kayıtları ve SaaS özellikleri gibi yüksek seviyeli bileşenlere kadar geniş bir yelpazeyi kapsar.

## Terraform Nasıl Çalışır?
- **Terraform**, bulut platformları ve diğer hizmetler üzerindeki kaynakları API'ler aracılığıyla oluşturur ve yönetir. Terraform, her platform veya hizmet için erişilebilir bir API olduğunda çalışabilir ve HashiCorp ve Terraform topluluğu tarafından yazılmış binlerce sağlayıcı (provider) bu amaçla kullanılabilir. Sağlayıcılar, Terraform'un bulut platformları, SaaS hizmetleri ve diğer API'lerle çalışmasına olanak tanır. Terraform'un çekirdek iş akışı üç aşamadan oluşur:
  1. **Yazma (Write)**: Kaynaklarınızı bir veya birden fazla bulut sağlayıcısı ve hizmette tanımlarsınız.
  2. **Planlama (Plan)**: Terraform, mevcut altyapıya ve konfigürasyonunuza dayanarak neleri yaratacağını, güncelleyeceğini veya yok edeceğini açıklayan bir plan oluşturur.
  3. **Uygulama (Apply)**: Onayınızla birlikte Terraform, önerilen işlemleri doğru sırayla gerçekleştirir ve kaynak bağımlılıklarına saygı gösterir.

## Neden Terraform?
- **Herhangi Bir Altyapıyı Yönetme**: Terraform, mevcut platform ve hizmetlerin çoğu için sağlayıcılar sunar ve ayrıca kendi sağlayıcınızı da yazabilirsiniz. Terraform, altyapıyı yönetirken değişmez bir yaklaşım benimser ve bu sayede hizmetlerinizi ve altyapınızı yükseltme veya değiştirme sürecindeki karmaşıklığı azaltır.
- **Altyapınızı İzleme**: Terraform, bir plan oluşturur ve altyapınızı değiştirmeden önce onayınızı ister. Aynı zamanda, gerçek altyapınızı bir durum dosyasında izler ve bu durum dosyası, ortamınız için bir kaynak olarak kabul edilir. Bu dosya, altyapınızın konfigürasyonunuza uygun olmasını sağlamak için yapılacak değişiklikleri belirler.
- **Değişiklikleri Otomatikleştirme**: Terraform konfigürasyon dosyaları deklaratif olup, altyapınızın son durumunu tanımlar. Kaynakları oluşturmak için adım adım talimatlar yazmanız gerekmez; Terraform, bağımlılıkları belirleyerek kaynakları paralel olarak yaratır veya değiştirir.
- **Konfigürasyonları Standartlaştırma**: Terraform, modüller adı verilen yeniden kullanılabilir konfigürasyon bileşenlerini destekler. Modüller, altyapı konfigürasyonlarının zaman kazandıran ve en iyi uygulamaları teşvik eden bileşenleridir. Bu modülleri Terraform Registry'den bulabilir veya kendi modüllerinizi yazabilirsiniz.

## Terraform Kurulumu
- **Kurulum**: Terraform'un kurulum süreci HashiCorp'un resmi web sitesinde ayrıntılı olarak açıklanmıştır. Kurulum işlemi platforma göre değişiklik gösterebilir, ancak temel adımlar genellikle benzerlik gösterir.

# Terraform Anahtar Kelimeler
## Providers (Sağlayıcılar)
- **Terraform Sağlayıcıları Nedir?**
  - Terraform, bulut sağlayıcıları, SaaS sağlayıcıları ve diğer API'lerle etkileşim kurmak için sağlayıcılar adı verilen eklentilere dayanır. Terraform konfigürasyonları, hangi sağlayıcıların gerektiğini belirtmelidir, böylece Terraform bu sağlayıcıları kurup kullanabilir. Bazı sağlayıcıların kullanılmadan önce yapılandırılması gerekebilir (örneğin, uç nokta URL'leri veya bulut bölgeleri gibi) .

- **Sağlayıcılar Ne Yapar?**
  - Her sağlayıcı, Terraform'un yönetebileceği kaynak türleri ve/veya veri kaynakları ekler. Her kaynak türü bir sağlayıcı tarafından uygulanır; sağlayıcılar olmadan Terraform herhangi bir altyapıyı yönetemez. Çoğu sağlayıcı, belirli bir altyapı platformunu (bulut veya yerel) yapılandırır. Sağlayıcılar ayrıca benzersiz kaynak adları için rastgele sayı oluşturma gibi yerel yardımcı programlar da sunabilir .

- **Sağlayıcı Belgeleri**
  - Her sağlayıcının, kaynak türleri ve bunların bağımsız değişkenlerini açıklayan kendi belgelendirmesi vardır. Terraform Registry, HashiCorp, üçüncü taraf satıcılar ve Terraform topluluğu tarafından geliştirilen geniş bir sağlayıcı yelpazesi için belgeler içerir. Bir sağlayıcının başlığındaki "Documentation" bağlantısını kullanarak belgelerine göz atabilirsiniz. Sağlayıcı belgeleri, versiyonlanmıştır; başlıktaki versiyon menüsünü kullanarak görüntülediğiniz versiyonu değiştirebilirsiniz  .

## Modules (Modüller)
- **Modüller Nedir?**
  - Modüller, birlikte kullanılan birden fazla kaynağın bulunduğu kapsayıcılardır. Bir modül, bir dizinde bir arada tutulan .tf ve/veya .tf.json dosyalarından oluşur. Modüller, Terraform ile kaynak yapılandırmalarını paketlemek ve yeniden kullanmak için ana yoldur .

- **Kök Modül (Root Module)**
  - Her Terraform konfigürasyonu en az bir modüle sahiptir; bu modül, ana çalışma dizinindeki .tf dosyalarında tanımlanan kaynaklardan oluşur. Bu modül kök modül olarak adlandırılır .

- **Çocuk Modüller (Child Modules)**
  - Bir Terraform modülü (genellikle bir konfigürasyonun kök modülü), başka modülleri çağırabilir ve bu modüllerin kaynaklarını konfigürasyona dahil edebilir. Başka bir modül tarafından çağrılan bir modül genellikle çocuk modül olarak adlandırılır. Çocuk modüller aynı konfigürasyon içinde birden fazla kez çağrılabilir ve birden fazla konfigürasyon aynı çocuk modülü kullanabilir .

- **Yayınlanmış Modüller**
  - Terraform, yerel dosya sisteminden modülleri yükleyebildiği gibi, bunları genel veya özel bir kayıt defterinden de yükleyebilir. Bu, başkaları tarafından yayınlanan modülleri kullanmanıza ve başkalarının kullanması için modüllerinizi yayınlamanıza olanak tanır. Terraform Registry, birçok yaygın altyapı türü için geniş bir halka açık Terraform modülleri koleksiyonuna ev sahipliği yapar. Bu modüller ücretsizdir ve Terraform, uygun kaynak ve versiyonu bir modül çağrı bloğunda belirttiğinizde bunları otomatik olarak indirebilir .

## State (Durum)
- **Terraform Durumu Nedir?**
  - Terraform, yönetilen altyapınız ve yapılandırmanız hakkında durum bilgisi depolamak zorundadır. Bu durum, Terraform tarafından gerçek dünya kaynaklarını yapılandırmanızla eşleştirmek, meta verileri takip etmek ve büyük altyapılar için performansı artırmak için kullanılır. Bu durum varsayılan olarak "terraform.tfstate" adlı yerel bir dosyada depolanır, ancak bunu HCP Terraform'da saklamanızı öneririz. HCP Terraform, durumu sürümlemeyi, şifrelemeyi ve ekibinizle güvenli bir şekilde paylaşmayı sağlar  .

- **Durumun Önemi**
  - Terraform, altyapınızda hangi değişiklikleri yapacağını belirlemek için durumu kullanır. Herhangi bir işlemden önce Terraform, durumu gerçek altyapı ile güncellemek için bir yenileme (refresh) gerçekleştirir. Terraform durumunun birincil amacı, uzaktaki bir sistemdeki nesneler ile yapılandırmanızda beyan edilen kaynak örnekleri arasında bağlantılar kurmaktır. Terraform, bir yapılandırma değişikliğine yanıt olarak uzaktaki bir nesne oluşturduğunda, o uzaktaki nesnenin kimliğini belirli bir kaynak örneği ile ilişkilendirir ve ardından gelecekteki yapılandırma değişikliklerine yanıt olarak bu nesneyi potansiyel olarak günceller veya siler  .

## Variables (Değişkenler) ve Outputs (Çıktılar)
- **Girdi Değişkenleri (Input Variables)**
  - Girdi değişkenleri, kullanıcıların bir Terraform modülünün davranışını kaynak kodunu değiştirmeden özelleştirmesine olanak tanır. Bu işlevsellik, modülleri farklı Terraform konfigürasyonlarında paylaşmanıza olanak tanır ve modülünüzü bileşen tabanlı ve yeniden kullanılabilir hale getirir .

- **Çıktı Değişkenleri (Output Variables)**
  - Çıktı değişkenleri, bir Terraform modülünün geri dönüş değerleri gibidir. Diğer modüller tarafından kullanılabilir veya son kullanıcıya çıktılar olarak gösterilebilir .

- **Yerel Değerler (Local Values)**
  - Yerel değerler, bir ifadeye kısa bir ad atamak için kullanılan bir kolaylık özelliğidir. Bu, kodun okunabilirliğini artırır ve tekrarlanan ifadelerden kaçınmanıza olanak tanır .


---

# 15. Gün - CI/CD Geliştirme ve Uygulamaları (Bölüm 2)

Staj programımızın on beşinci gününde CI/CD süreçlerine devam ettik ve bu kapsamda Continuous Delivery (Sürekli Teslimat) ile Continuous Deployment (Sürekli Dağıtım) konularını inceledik. Ayrıca, dağıtım yaklaşımları ve GitOps gibi modern DevOps pratikleri hakkında detaylı bilgiler edindik.

## Continuous Delivery (Sürekli Teslimat)

### Continuous Delivery Nedir?
- **Continuous Delivery**, yazılım geliştirme pratiğidir ve kod değişikliklerinin otomatik olarak üretime hazırlık aşamasına getirilmesini sağlar. Bu yöntem, modern uygulama geliştirme süreçlerinin temel taşlarından biridir ve Continuous Integration (Sürekli Entegrasyon) pratiğini genişleterek, tüm kod değişikliklerinin yapı aşamasından sonra bir test veya üretim ortamına dağıtılmasını sağlar. Continuous Delivery, birim testlerinin ötesine geçerek yazılım güncellemelerinin çeşitli açılardan doğrulanmasını ve müşteri yayını öncesinde sorunların tespit edilmesini sağlar.

### Delivery ve Deployment Arasındaki Fark
- **Continuous Delivery** ile her kod değişikliği, yapıldıktan sonra test edilir ve ardından üretim dışı bir test veya hazırlık ortamına gönderilir. Üretim dağıtımından önce birden fazla paralel test aşaması olabilir. **Continuous Deployment** (Sürekli Dağıtım) ile olan fark, üretim ortamına güncelleme yapmak için manuel bir onay sürecinin bulunmasıdır. Sürekli Dağıtımda ise bu süreç otomatik olarak gerçekleşir. Continuous Delivery, yazılım teslimat sürecini otomatikleştirir ve her bir değişiklik, geliştirici tarafından tetiklenen bir akışla test edilir ve hazırlık ortamına gönderilir.

### Continuous Delivery'nin Faydaları
- **Geliştirici Verimliliğini Artırır**: Geliştiricileri manuel görevlerden kurtararak, hataların ve müşteri sorunlarının azalmasına yardımcı olur.
- **Hataların Erken Tespiti**: Daha sık ve kapsamlı testlerle hataların erken tespit edilmesini sağlar.
- **Hızlı Güncelleme Teslimatı**: Güncellemelerin daha hızlı ve düzenli bir şekilde müşterilere ulaştırılmasını sağlar.
- **Yazılım Teslim Sürecini Otomatikleştirir**: Kod değişikliklerinin otomatik olarak yapılandırılması, test edilmesi ve üretime hazır hale getirilmesi sürecini sağlar.

## Continuous Deployment (Sürekli Dağıtım)

### Continuous Deployment Nedir?
- **Continuous Deployment (Sürekli Dağıtım)**, yazılım geliştirme süreçlerinde yazılım işlevlerinin otomatik olarak ve sık sık dağıtılmasını sağlayan bir yaklaşımdır. Continuous Deployment, Continuous Delivery ile benzer bir yaklaşımdır ancak aralarındaki fark, Continuous Deployment'da üretim dağıtımının manuel onay olmadan otomatik olarak yapılmasıdır.

### Continuous Deployment'ın Faydaları
- **Daha Hızlı Yazılım Teslimatı**: Geliştirme süreci dağıtım ve yayın için duraklamadığından kodlama süreci çok daha hızlıdır. Bir özellik hazır olduğunda, kullanıcılar hemen kullanmaya başlayabilir ve geri bildirim verebilir.
- **Zamanın Optimal Kullanımı**: Otomatik dağıtım, ekibin sürekli olarak görevlerini yeniden önceliklendirmesine olanak tanır ve manuel dağıtıma zaman ayırmak yerine diğer görevlere odaklanmalarını sağlar.
- **Azaltılmış Risk ve Maliyet**: Geliştirme risklerini azaltmaya yardımcı olur. Sürüm süreçleri daha küçük ve anlaşılır hale gelir, bu da hata tespitini ve düzeltmesini kolaylaştırır.
- **Müşteri Geri Bildirimi ve Memnuniyeti**: Yeni özellikler ve iyileştirmeler üretime anında dağıtıldığı için müşteri geri bildirimi daha hızlı alınır.

## Dağıtım Yaklaşımları

### Push Yöntemi
- **Push yöntemi**: Yazılım güncellemelerinin doğrudan hedef sistemlere iletilmesi stratejisidir. Bu yöntemde güncellemeler merkezi bir sunucudan otomatik olarak dağıtılır ve hedef sistemlere hızlı bir şekilde uygulanır. Ancak bu yöntem birkaç kritik güvenlik hususu gerektirir:
  - **Kimlik Doğrulama ve Yetkilendirme**: Güncellemeleri gönderen sistemler ve kullanıcılar dikkatlice kontrol edilmeli ve doğrulanmalıdır.
  - **Şifreleme Protokolleri**: Verilerin kötü niyetli kişiler tarafından ele geçirilmesini önlemek için veri iletimi sırasında şifreleme protokolleri kullanılmalıdır.
  - **Güncellemelerin Bütünlüğü**: Güncellemelerin değiştirilmediğinden emin olmak için dijital imzalar ve hash fonksiyonları kullanılmalıdır.
  - **Geri Alma Mekanizmaları**: Güncelleme hatalı olursa geri alınabilecek mekanizmaların bulunması gereklidir.
  - **Güvenlik Testleri**: Güncellemeler kapsamlı güvenlik testlerinden geçmelidir.

### Pull Yöntemi
- **Pull yöntemi**: Yazılım güncellemelerinin merkezi bir sunucudan hedef sistemler tarafından talep edilmesi stratejisidir. Bu yöntemde, sistemler periyodik olarak güncellemeleri kontrol eder ve gerektiğinde indirir.
  - **Avantajlar**: Sistemlerin bağımsız olarak güncellenmesine olanak tanır ve ağ yükünü azaltabilir.
  - **Zorluklar**: Güncellemelerin zamanlaması ve yöntemi her sistemin konfigürasyonuna bağlıdır, bu da güncelleme sürecinde belirsizlik yaratabilir.

## GitOps

### GitOps Nedir?
- **GitOps**, uygulama geliştirme süreçleri için DevOps yaklaşımlarının uygulanmasını sağlayan bir kavramdır. Bu yaklaşım, tüm süreçlerin Git üzerinden kontrol edilebileceği fikrine dayanır. GitOps, versiyon kontrol, iş birliği, uyumluluk ve CI/CD araçlarını altyapı otomasyonu için kullanır. GitOps, ekipler arasında daha iyi iş birliği ve daha hızlı koordinasyon sağlar, bu da hataların ve sorunların azalmasına katkıda bulunur.

### GitOps Araçları: ArgoCD ve FluxCD
- **ArgoCD** ve **FluxCD** gibi araçlar, Kubernetes tabanlı uygulamaların dağıtımını kolaylaştıran araçlardır. Bu araçlar, Git'teki değişiklikleri izler ve uygulamaları otomatik olarak günceller. Uygulama geliştiricileri kodlarını değiştirdiğinde, bu ürünler otomatik olarak bu değişiklikleri algılar ve güncellenmiş uygulamaları dağıtır.

### ArgoCD Nedir?
- **ArgoCD**, sürekli teslimat sürecini destekleyen bir araçtır. ArgoCD, hedef ortama otomatik olarak uygulama durumlarını dağıtır. Bu aracın temel özelliği, dağıtımlarınızı uygulama deposunda yapılan değişikliklerle senkronize etmektir. Bu, otomasyon, denetlenebilirlik ve kullanım kolaylığı sağlar.

### ArgoCD Mimarisi ve Yapısı
- **API/Web Sunucusu**: Ana bileşenlerden biri olan API/Web Sunucusu, ArgoCD'nin kullanıcı arayüzünü ve API hizmetlerini sağlar.
- **Repo Sunucusu**: Kaynak kodunun saklandığı depoyu kontrol eder. Klonlama işlemleri ve Kubernetes manifest dosyalarının oluşturulması bu sunucu tarafından gerçekleştirilir.
- **Uygulama Kontrolcüsü**: Kubernetes kümesinin yönetimini sağlar. Kullanıcı arayüzünde gösterilen gerçek zamanlı verilerin toplanması, ArgoCD'de belirlenen uygulamaların dağıtımı ve kullanıcı tarafından yapılan işlemler bu kontrolcü sayesinde gerçekleştirilir.

### ArgoCD'nin Avantajları
- **Kullanıcı Arayüzü**: ArgoCD, depo senkronizasyon durumu, dağıtım ve pod sağlık kontrolleri, ve projelerinizin genel durumu gibi bilgileri gerçek zamanlı olarak yönetmenize olanak tanıyan işlevsel bir kullanıcı arayüzüne sahiptir.
- **Pull Modeli**: Geleneksel CI/CD araçlarının kullandığı Push Modeli yerine Pull Modelini kullanır. Bu modelde, ArgoCD depo değişikliklerini izler ve Kubernetes kümesine yeni etiketle senkronize olan imajı dağıtır.

---
