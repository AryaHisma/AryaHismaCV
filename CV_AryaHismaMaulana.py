import streamlit as st
from PIL import Image


# Set page config
st.set_page_config(
    page_title="Aplikasi Saya",
    page_icon="https://example.com/icon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Set CSS
with open('assets/style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



# Create columns for layout
col1, col2 = st.columns([1, 2])


with col1:
       
    with st.container(height=500, border=False):
        # --- IMAGE ---
        image = Image.open("assets/Untitled.png")
        st.image(image)
        
    with st.container(height=1000, border=True):
        st.header("**DATA PRIBADI**")
        st.markdown('''
                    <p><strong>Tempat/Tanggal Lahir</strong><br>
                    Banda Aceh / 2 Oktober 1990</p>
                    ''', unsafe_allow_html=True)
        
        st.markdown('''
                    <p><strong>Jenis Kelamin</strong><br>
                    Laki-laki</p>
                    ''', unsafe_allow_html=True)
        
        st.markdown('''
                    <p><strong>Agama</strong><br>
                    Islam</p>
                    ''', unsafe_allow_html=True)
        
        st.markdown('''
                    <p><strong>Kewarganegaraan</strong><br>
                    Indonesia</p>
                    ''', unsafe_allow_html=True)
        
        # Load Font Awesome CSS
        st.markdown("""
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        """, unsafe_allow_html=True)
        
        # Kontak header
        st.header("KONTAK")

        # Kontak details with icons
        st.markdown("""
            <p><i class="fas fa-phone-alt"></i>   0823 6644 28**</p>
            <p><i class="fas fa-envelope"></i> aryahisma@yahoo.co.id</p>
            <p><i class="fas fa-map-marker-alt"></i> JL. Jalan. Tgk. Adee V Desa Doy. 
            Kecamatan Ulee Kareng. Kota Banda Aceh. Propinsi Aceh, 23715</p>
            """, unsafe_allow_html=True)
        
    #    JL. Jalan. Tgk. Adee V Desa Doy. 
    #         Kecamatan Ulee Kareng. Kota Banda Aceh. Propinsi Aceh, 23715 
        
        # Skill header
        st.header("SKILL")

        # Create columns for skills and progress bars
        col_skil, col_prog = st.columns([1, 1])

        with col_skil:
            st.markdown("**Tableau**")
            st.markdown("**Power BI**")
            st.markdown("**Python (Machine Learning)**")

        with col_prog:
            progress_bar_style = """
        <style>
        .stProgress > div > div > div > div {
            background-color: blue;
        }
        </style>
    """
            st.markdown(progress_bar_style, unsafe_allow_html=True)

            st.progress(80)
            st.write("")  # Menambahkan jarak
            st.progress(80)
            st.write("")  # Menambahkan jarak
            st.progress(80)
        
        
        # Load Font Awesome CSS
        st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
        .social-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            background-color: white;
            color: black;
            border: 2px solid black;
            border-radius: 5px;
            padding: 10px 15px;
            margin: 5px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s, color 0.3s;
             }
        .social-button:hover {
            background-color: black;
            color: white;
            }
        .social-button i {
            margin-right: 8px;
            }
        </style>
        """, unsafe_allow_html=True)

        # Social Media header
        st.header("SOCIAL MEDIA")

        # Social media buttons
        st.markdown("""
        <a href="https://www.linkedin.com/in/arya-hisma-maulana" class="social-button">
            <i class="fab fa-linkedin"></i> LinkedIn
        </a>
        <a href="https://www.instagram.com/aryahisma" class="social-button">
          <i class="fab fa-instagram"></i> Instagram
      </a>
     <a href="https://github.com/AryaHisma" class="social-button">
         <i class="fab fa-github"></i> GitHub
     </a>
        """, unsafe_allow_html=True)
    
with col2:
    
        st.markdown("# Arya Hisma Maulana, ST")
          

        # Load custom CSS
        st.markdown("""
            <style>
            .profile-header {
                font-size: 32px;
                font-weight: bold;
                color: #dd3f3f;
                border-bottom: 3px solid #007bff;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            .profile-text {
                font-size: 18px;
                color: #555;
                line-height: 1.6;
            }
            </style>
            """, unsafe_allow_html=True)

        # Header
        st.markdown('<div class="profile-header">PROFIL</div>', unsafe_allow_html=True)

        # Profile text
        st.markdown('''
        <div class="profile-text">
Seorang data analis dengan pengalaman lebih dari 5 tahun di bidang analisis data, saya memiliki keterampilan mendalam dalam:
Pembersihan, Transformasi, dan Penyimpanan Data: Menggunakan Tableau Prep dan Python untuk membersihkan, mentransformasi, dan menyimpan data dalam data warehouse, memastikan konsistensi dan aksesibilitas data.
Visualisasi Data: Membuat visualisasi data interaktif dengan Tableau dan Power BI, mendesain dashboard yang mendukung pengambilan keputusan strategis.
Uji Statistik dan Machine Learning: Melakukan analisis statistik dan menerapkan algoritma machine learning dengan Python, termasuk uji korelasi, analisis regresi, dan analisis cluster. Mengembangkan model untuk prediksi dan klasifikasi, serta visualisasikan hasilnya untuk komunikasi yang efektif.
Kombinasi keterampilan teknis ini memungkinkan saya untuk memberikan wawasan yang berharga dan mendukung keputusan berbasis data di berbagai konteks bisnis.

</div>
        ''', unsafe_allow_html=True)
                
        # st.header("Profil")
        # st.markdown('''Seorang profesional Pemasaran Digital dengan pengalaman 
        #             lebih dari 1 tahun dalam mengembangkan dan melaksanakan strategi 
        #             pemasaran online yang berhasil. Memiliki pemahaman mendalam tentang 
        #             berbagai platform digital dan alat analitik. Terampil dalam 
        #             meningkatkan visibilitas online, memperkuat merek, dan meningkatkan 
        #             konversi.''')

        # Load custom CSS
        st.markdown("""
            <style>
            .education-header {
                font-size: 32px;
                font-weight: bold;
                color: #dd3f3f;
                border-bottom: 3px solid #007bff;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            .education-item {
                font-size: 18px;
                color: #555;
                margin-bottom: 10px;
            }
            .education-item strong {
                font-weight: bold;
            }
            .education-details {
                margin-left: 20px;
                font-size: 16px;
                color: #666;
            }
            </style>
            """, unsafe_allow_html=True)

        # Header
        st.markdown('<div class="education-header">RIWAYAT PENDIDIKAN</div>', unsafe_allow_html=True)

        # Education details
        st.markdown('''
        <div class="education-item">
            <strong>S1 Teknik Sipil Universitas Syiah Kuala</strong>
            <div class="education-details">
                - Banda Aceh, 2008-2013<br>
                - Lulus dengan predikat Pujian, IPK 3.45
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        
        # st.header("Riwayat Pendidikan")
        # st.markdown('''
        #             **S1 Teknik Sipil Universitas Syiah Kuala**
        #             - Banda Aceh, 2008-2013
        #             - Lulus dengan predikat Pujian, IPK 3.45
        #             ''')
        
        
        # Load custom CSS
        st.markdown("""
            <style>
            .job-header {
                font-size: 32px;
                font-weight: bold;
                color: #dd3f3f;
                border-bottom: 3px solid #007bff;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            .job-item {
                font-size: 18px;
                color: #555;
                margin-bottom: 10px;
            }
            .job-company {
                font-weight: bold;
                color: #333;
            }
            .job-date {
                font-style: italic;
                color: #777;
            }
            .job-description {
                margin-left: 20px;
                font-size: 16px;
                color: #666;
                line-height: 1.6;
            }
            </style>
                """, unsafe_allow_html=True)

        # Header
        st.markdown('<div class="job-header">RIWAYAT PEKERJAAN</div>', unsafe_allow_html=True)

        # Job details
        st.markdown('''
<div class="job-item">
    <div class="job-company">PT Pembangunan Perumahan (Persero) .Tbk</div>
    <div class="job-date">Jakarta, Sep 2018 - Saat Ini</div>
    <div class="job-description">
        <strong> - Melakukan Pembersihan, Transformasi, dan Penyimpanan Data di Data Warehouse</strong><br>
        Saya bertanggung jawab untuk melakukan pembersihan dan transformasi data menggunakan Tableau Prep. Proses ini mencakup identifikasi dan penghapusan data duplikat, mengatasi data yang hilang, dan standardisasi format data. Saya juga memanfaatkan extension analytics dengan Python untuk mengotomatiskan dan meningkatkan efisiensi proses transformasi data. Setelah data dibersihkan dan ditransformasikan, saya menyimpannya ke dalam data warehouse yang terintegrasi untuk memastikan aksesibilitas dan konsistensi data bagi tim analitik lainnya.
    </div>
    <div class="job-description">
        <strong> - Visualisasi Data</strong><br>
        Saya memiliki pengalaman dalam membuat visualisasi data yang informatif dan interaktif menggunakan Tableau dan Power BI. Saya merancang dashboard yang intuitif dan mudah dipahami, yang membantu dalam pengambilan keputusan strategis berdasarkan data. Visualisasi yang saya buat mencakup berbagai jenis grafik, peta, dan laporan yang memberikan wawasan mendalam mengenai tren dan pola dalam data.
    </div>
    <div class="job-description">
        <strong> - Melakukan Uji Statistik dan Machine Learning</strong><br>
        Dalam pekerjaan saya, saya juga melakukan uji statistik dan penerapan algoritma machine learning menggunakan Python. Saya melakukan analisis statistik seperti uji korelasi, analisis regresi, dan analisis cluster untuk memahami karakteristik dan hubungan dalam data. Selain itu, saya mengembangkan model machine learning untuk prediksi dan klasifikasi. Hasil dari analisis dan model tersebut kemudian saya visualisasikan menggunakan Tableau untuk memudahkan interpretasi dan komunikasi hasil kepada tim dan stakeholder lainnya.
    </div>
</div>
''', unsafe_allow_html=True)
        
        
        # st.header("Riwayat Pekerjaan")
        # st.markdown('''
        #             **PT Pembangunan Perumahan (Persero) .Tbk**
        #             Jakarta, Sep 2018 - Saat Ini
                    
        #             - Melakukan Pembersihan, Transformasi, dan Penyimpanan Data di Data Warehouse
        # Saya bertanggung jawab untuk melakukan pembersihan dan transformasi data menggunakan Tableau Prep. Proses ini mencakup identifikasi dan penghapusan data duplikat, mengatasi data yang hilang, dan standardisasi format data. Saya juga memanfaatkan extension analytics dengan Python untuk mengotomatiskan dan meningkatkan efisiensi proses transformasi data. Setelah data dibersihkan dan ditransformasikan, saya menyimpannya ke dalam data warehouse yang terintegrasi untuk memastikan aksesibilitas dan konsistensi data bagi tim analitik lainnya.

        #             - Visualisasi Data 
        # Saya memiliki pengalaman dalam membuat visualisasi data yang informatif dan interaktif menggunakan Tableau dan Power BI. Saya merancang dashboard yang intuitif dan mudah dipahami, yang membantu dalam pengambilan keputusan strategis berdasarkan data. Visualisasi yang saya buat mencakup berbagai jenis grafik, peta, dan laporan yang memberikan wawasan mendalam mengenai tren dan pola dalam data.

        #             - Melakukan Uji Statistik dan Machine Learning
        # Dalam pekerjaan saya, saya juga melakukan uji statistik dan penerapan algoritma machine learning menggunakan Python. Saya melakukan analisis statistik seperti uji korelasi, analisis regresi, dan analisis cluster untuk memahami karakteristik dan hubungan dalam data. Selain itu, saya mengembangkan model machine learning untuk prediksi dan klasifikasi. Hasil dari analisis dan model tersebut kemudian saya visualisasikan menggunakan Tableau untuk memudahkan interpretasi dan komunikasi hasil kepada tim dan stakeholder lainnya.
        #             ''')
        
        # Load custom CSS
        st.markdown("""
            <style>
            .job-header {
                font-size: 32px;
                font-weight: bold;
                color: #dd3f3f;
                border-bottom: 3px solid #007bff;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            .job-item {
                font-size: 18px;
                color: #555;
                margin-bottom: 10px;
            }
            .job-company {
                font-weight: bold;
                color: #333;
            }
            .job-date {
                font-style: italic;
                color: #777;
            }
            .job-description {
                margin-left: 20px;
                font-size: 16px;
                color: #666;
                line-height: 1.6;
            }
            </style>
                """, unsafe_allow_html=True)

        # Header
        st.markdown('<div class="job-header">PENGALAMAN PELATIHAN</div>', unsafe_allow_html=True)

        # Job details
        st.markdown('''
<div class="job-item">
    <div class="job-company">ALGORITMA ACADEMY (Data Analytics Specialization)</div>
    <div class="job-date">Jakarta, Nov 2023 - Jan 2024</div>
    <div class="job-description">
        <strong> - Python for Data Analytics</strong><br>
        <strong> - Exploratory Data Analysis</strong><br>
        <strong> - Data Wrangling and Visualization</strong><br>
        <strong> - SQL Query and Capstone Project</strong><br>
        <strong> - Intoduction to Machine Learning</strong><br>
        </div>
    
</div>
''', unsafe_allow_html=True)  
        
        st.markdown('''
<div class="job-item">
    <div class="job-company">Digital Talent Scholarship Kominfo (UI/UX Design)</div>
    <div class="job-date">Jakarta, Agu 2022 - Okt 2022</div>
    <div class="job-description">
        <strong> - UX Design Process</strong><br>
        </div>
    
</div>
''', unsafe_allow_html=True) 
        
        # Load custom CSS
        st.markdown("""
            <style>
            .job-header {
                font-size: 32px;
                font-weight: bold;
                color: #dd3f3f;
                border-bottom: 3px solid #007bff;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            .job-item {
                font-size: 18px;
                color: #555;
                margin-bottom: 10px;
            }
            .job-company {
                font-weight: bold;
                color: #333;
            }
            .job-date {
                font-style: italic;
                color: #777;
            }
            .job-description {
                margin-left: 20px;
                font-size: 16px;
                color: #666;
                line-height: 1.6;
            }
            </style>
                """, unsafe_allow_html=True)

        # Header
        st.markdown('<div class="job-header">PENGALAMAN ORGANISASI</div>', unsafe_allow_html=True)

        # Job details
        st.markdown('''
<div class="job-item">
    <div class="job-company">IKAFT USK JABAJAB</div>
    <div class="job-date">Jakarta, Sep 2018 - Saat Ini</div>
    <div class="job-description">
        <strong> - Menyelenggarakan musyawarah besar organisasi</strong><br>
        <strong> - Menyelenggarakan pelatihan bagi alumni</strong><br>
        </div>
    
</div>
''', unsafe_allow_html=True)
        
      
        
        