-- BUAT DATABASE trainingdb
CREATE DATABASE trainingdb;
-- PILIH DATABASE YANG SUDAH KITA BUAT
USE trainingdb;

-- BUAT FILE
CREATE TABLE anggota(
	id int PRIMARY KEY AUTO_INCREMENT,
    nik varchar(255) UNIQUE,
    nama varchar(255) NOT NULL,
    usia int,
    tgl_lahir DATE,
    alamat VARCHAR(255),
    telp VARCHAR(255)
);