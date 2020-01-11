# RIDHO MARHABAN
import pymysql
from flask import Flask, session
import config

db = cursor = None

class MPengguna:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def openDB(self):
        global db, cursor
        db = pymysql.connect(
            config.DB_HOST,
            config.DB_USER,
            config.DB_PASSWORD,
            config.DB_NAME)
        cursor = db.cursor()
        print("connected")

    def closeDB(self):
        global db, cursor
        db.close()

    def authenticate(self):
        self.openDB()
        cursor.execute("SELECT COUNT(*) FROM accounts WHERE username = '%s' AND password = MD5('%s')" % (self.username,self.password))
        count_account = (cursor.fetchone())[0]
        self.closeDB()
        return True if count_account>0 else False

    def userLevel(self):
        self.openDB()
        cursor.execute("SELECT * FROM accounts WHERE username = '%s' AND password = MD5('%s')" % (self.username,self.password))
        account = (cursor.fetchone())
        self.closeDB()
        if account[4] == 'admin':
            return 'admin'
        elif account[4] == 'user':
            return 'user'

    def accName(self):
        self.openDB()
        cursor.execute("SELECT * FROM accounts WHERE username = '%s' AND password = MD5('%s')" % (self.username,self.password))
        account = (cursor.fetchone())
        nama = account[1]
        self.closeDB()
        return nama

# ================== ADMIN =========================
            # ============= TABEL AKUN ===================
    def showAllAcc(self):
        self.openDB()
        cursor.execute(" SELECT * FROM accounts")
        accounts = (cursor.fetchall())
        container = []
        for i in accounts:
            container.append((i))
        self.closeDB()
        return container

    def insertDBAcc(self, data):
        self.openDB()
        cursor.execute("INSERT INTO accounts VALUES('%s','%s','%s',MD5('%s'),'%s')" % data)
        db.commit()
        self.closeDB()

    def getAccbyID(self, id_account):
        self.openDB()
        cursor.execute("SELECT * FROM accounts WHERE id='%s'" % id_account)
        data = cursor.fetchone()
        return data

    def updateDBAcc(self, data):
        self.openDB()
        cursor.execute("UPDATE accounts SET name='%s', username='%s', password=MD5('%s'), rule='%s' WHERE id=%s" % data)
        db.commit()
        self.closeDB()

    def deleteDBacc(self, id_account):
        self.openDB()
        cursor.execute("DELETE FROM accounts WHERE id=%s" % id_account)
        db.commit()
        self.closeDB()

            # ============= TABEL PEMBAYARAN ====================

    def selectDBPay(self):
        self.openDB()
        cursor.execute("SELECT * FROM pembayaran")
        container = []
        for id_pembayaran, tanggal, nim, nama, prodi, semester, id_biaya, jml_pembayaran, jenis_pembayaran in cursor.fetchall():
            container.append((id_pembayaran, tanggal, nim, nama, prodi, semester, id_biaya, jml_pembayaran, jenis_pembayaran))
        self.closeDB()
        return container

    def insertDBPay(self, data):
        self.openDB()
        cursor.execute("INSERT INTO pembayaran (tanggal, nim, nama, prodi, semester, id_biaya, jml_pembayaran, jenis_pembayaran) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % data)
        db.commit()
        self.closeDB()

    def getDBbyNoPay(self, id_pembayaran):
        self.openDB()
        cursor.execute("SELECT * FROM pembayaran WHERE id_pembayaran='%s'" % id_pembayaran)
        data = cursor.fetchone()
        return data

    def updateDBPay(self, data):
        self.openDB()
        cursor.execute("UPDATE pembayaran SET tanggal='%s', nim='%s', nama='%s', prodi='%s', semester='%s', id_biaya='%s', jml_pembayaran='%s', jenis_pembayaran='%s' WHERE id_pembayaran=%s" % data)
        db.commit()
        self.closeDB

    def deleteDBPay(self, id_pembayaran):
        self.openDB()
        cursor.execute("DELETE FROM pembayaran WHERE id_pembayaran=%s" % id_pembayaran)
        db.commit()
        self.closeDB()

            # ============= TABEL DETAIL PEMBAYARAN =============

    def showAllDetail(self):
        self.openDB()
        cursor.execute(" SELECT * FROM detail_pembayaran ")
        details = (cursor.fetchall())
        container = []
        for i in details:
            container.append((i))
        self.closeDB()
        return container

    def insertDBDetail(self, data):
        self.openDB()
        cursor.execute("INSERT INTO detail_pembayaran (id_biaya, Semester, Sumbangan, Pra_Kuliah, her_registrasi, SPP_Tetap, SPP_Variable, UTS, UAS, total_biaya) VALUES('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()

    def getDBbyNoDetail(self, Id_Detail):
        self.openDB()
        cursor.execute("SELECT * FROM detail_pembayaran WHERE Id_Detail='%s'" % Id_Detail)
        data = cursor.fetchone()
        return data

    def updateDBDetail(self, data):
        self.openDB()
        cursor.execute("UPDATE detail_pembayaran SET Id_Biaya='%s', Semester='%s', Sumbangan='%s', Pra_Kuliah='%s', her_registrasi='%s', SPP_Tetap='%s', SPP_Variable='%s', UTS='%s', UAS='%s', total_biaya='%s' WHERE Id_Detail=%s" % data)
        db.commit()
        self.closeDB()

    def deleteDBDetail(self, id_detail):
        self.openDB()
        cursor.execute("DELETE FROM detail_pembayaran WHERE Id_Detail=%s" % id_detail)
        db.commit()
        self.closeDB()

            # ============= TABEL MAHASISWA ==============
    def showAllM(self):
        self.openDB()
        cursor.execute(" SELECT * FROM mahasiswa")
        mahasiswa = (cursor.fetchall())
        container = []
        for i in mahasiswa:
            container.append((i))
        self.closeDB()
        return container

    def insertDB(self, data):
        self.openDB()
        cursor.execute("INSERT INTO mahasiswa VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % data)
        db.commit()
        self.closeDB()

    def deleteDB(self, id_account):
        self.openDB()
        cursor.execute("DELETE FROM mahasiswa WHERE id_account=%s" % id_account)
        db.commit()
        self.closeDB()

    def getDBbyID(self, id_account):
        self.openDB()
        cursor.execute("SELECT * FROM mahasiswa WHERE id_account='%s'" % id_account)
        data = cursor.fetchone()
        return data

    def updateDB(self, data):
        self.openDB()
        cursor.execute("UPDATE mahasiswa SET nim='%s', nama='%s', alamat='%s', tempat_lahir='%s', tgl_lahir='%s', jenis_kelamin='%s', agama='%s', prodi='%s', fakultas='%s', semester=%s, angkatan=%s WHERE id_account=%s" % data)
        db.commit()
        self.closeDB()

# ================ USER ===============
    def showDataM(self):
        self.openDB()
        cursor.execute(" SELECT * FROM mahasiswa WHERE nama='%s' " % session['name'])
        mahasiswa = (cursor.fetchall())
        container = []
        for i in mahasiswa:
            container.append((i))
        self.closeDB()
        return container

    def selectDBPayUser(self):
        self.openDB()
        cursor.execute("SELECT * FROM pembayaran WHERE nim=%s" % session['username'])
        container = []
        for id_pembayaran, tanggal, nim, nama, prodi, semester, id_biaya, jml_pembayaran, jenis_pembayaran in cursor.fetchall():
            container.append((id_pembayaran, tanggal, nim, nama, prodi, semester, id_biaya, jml_pembayaran, jenis_pembayaran))
        self.closeDB()
        return container




        
