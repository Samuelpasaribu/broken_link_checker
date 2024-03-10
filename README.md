# Broken Link Checker

![GitHub last commit](https://img.shields.io/github/last-commit/username/repository)
![GitHub top language](https://img.shields.io/github/languages/top/username/repository)

This is a simple Python script to check for broken links on a website. It utilizes the `requests`, `BeautifulSoup`, and `colorama` libraries to fetch web pages, parse HTML, and provide colored output in the terminal.

## Usage

### Prerequisites

Before running the script, make sure you have Python 3 installed on your system. You can install the required libraries using pip:

```bash
pip3 install requests beautifulsoup4 colorama
```

### Running the Script

To check for broken links on a website, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Samuelpasaribu/broken_link_checker.git
```

2. Navigate to the cloned directory:

```bash
cd broken_link_checker
```

3. Run the script:

```bash
python3 1.py
```

or

```bash
python3 2.py
```

4. Enter the website URL when prompted.

### Example

```bash
Enter website URL: https://www.samuelpasaribu.com
```

### Output

The script will display the status of each link found on the website:

- Broken links are displayed in red.
- Working links are displayed in green.
- Errors encountered during link checking are displayed in yellow.

## Perbedaan Antara Kode Pertama dan Kode Kedua

### Kode Pertama:

**Fungsi Pengecekan Link:**
- Menggunakan metode `requests.head()` untuk memeriksa status kode HTTP dari setiap tautan.
- Hanya menandai tautan sebagai "Broken" jika status kode bukan 200.

**Tampilan Output:**
- Menggunakan warna teks dari pustaka `colorama` untuk membedakan tautan yang rusak dengan tautan yang berfungsi.

**Penanganan Kesalahan:**
- Menggunakan blok `try-except` untuk menangani kesalahan saat memeriksa tautan, seperti kesalahan koneksi atau respons tidak valid.

### Kode Kedua (yang baru):

**Fungsi Pengecekan Link:**
- Sama seperti kode pertama, menggunakan metode `requests.head()` untuk memeriksa status kode HTTP dari setiap tautan.
- Khususnya menandai tautan sebagai "404 Error" jika status kode adalah 404 (Not Found).

**Tampilan Output:**
- Menambahkan pesan "Checking links on {url}" sebelum memulai pengecekan tautan.
- Tautan yang menghasilkan status kode 404 ditampilkan dengan warna merah dan label "[404 Error]".

**Penanganan Kesalahan:**
- Sama seperti kode pertama, menggunakan blok `try-except` untuk menangani kesalahan saat memeriksa tautan.

Dengan kode yang baru, tampilan output menjadi lebih informatif dengan menunjukkan status kode 404 secara eksplisit untuk tautan yang tidak ditemukan. Hal ini membantu pengguna untuk lebih mudah mengidentifikasi tautan yang rusak atau mati.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
