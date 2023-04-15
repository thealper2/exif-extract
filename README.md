# exif-extract

Bir fotoğraf dosyası hakkında metadata bilgilerini göstermeye yarayan bir araçtır.

## Gereksinimler

exif-extract aşağıdaki kütüphaneleri kullanır.

* Colorama
* Pillow

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/exif-extract.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| --image   | Image. Bilgi alınacak dosyayı belirtmek için kullanılır. |
```bash
usage: exif_extract.py [-h] [--image image]

Exif extractor

options:
  -h, --help  show this help message and exit
  -image      image file
```

## Örnekler

```python
python3 exif_extract.py --image test.jpg
```
