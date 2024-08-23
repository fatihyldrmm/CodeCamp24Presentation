#!/bin/bash

echo "Aranacak kelimeyi girin:"
read word
echo "Dosya adını girin:"
read file

if [[ ! -f "$file" ]]; then
  echo "Dosya bulunamadı!"
  exit 1
fi

count=$(grep -o -w "$word" "$file" | wc -l)
echo "Kelime '$word' dosyada $count kez geçiyor."
