# CASE-2 Ansible ile Playbook oluşturma

## Playbook Açıklaması

Bu Ansible playbook'u, localhost üzerinde bir dosya oluşturup, dosyanın erişim izinlerini ayarlayıp, içine veri yazıp, bu veriyi konsola yazdırıp, ardından dosyanın içeriğine yeni veri ekleyip tekrar konsola yazdırarak başka bir dizine kopyalar.

## Adımlar

1. **Dosya Oluşturma ve İzinleri Ayarlama:**
   - `/tmp/hello_world.txt` dosyası oluşturulur ve dosya izinleri `0644` olarak ayarlanır.

2. **Dosyaya Veri Yazma:**
   - Dosyaya "Hello World" yazılır.

3. **Dosya İçeriğini Konsola Yazdırma:**
   - Dosyanın içeriği (`Hello World`) konsola yazdırılır.

4. **Dosyanın İçeriğine Veri Ekleme:**
   - Dosyanın mevcut içeriğinin (Hello World) altına "Merhaba Dünya" eklenir.

5. **Güncellenmiş Dosya İçeriğini Konsola Yazdırma:**
   - Dosyanın güncellenmiş içeriği konsola yazdırılır.

6. **Yedekleme Dizininin Kontrolü ve Oluşturulması:**
   - `/tmp/backup` dizini mevcut değilse oluşturulur.

7. **Dosyanın Başka Bir Dizinine Kopyalanması:**
   - `/tmp/hello_world.txt` dosyası `/tmp/backup/hello_world.txt` dizinine kopyalanır.

## Kullanım

Bu playbook'u çalıştırmak için aşağıdaki adımları yapabilirsiniz:

1. Playbook dosyasını `playbook.yml` adıyla kaydedin.
2. Terminalden aşağıdaki komutu çalıştırın:

   ```bash
   ansible-playbook playbook.yml



![output](screenshots\output.jpg)
