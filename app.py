# Ridho Marhaban
from flask import Flask, render_template, session, request, redirect, url_for
from models import MPengguna

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefg12345'

# ======== LOGIN ================================================================================================

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        if 'rule' in session and session['rule'] == 'admin':
            rule = session['rule']
            if 'name' in session:
                name = session['name']
                return render_template('admin.html', username=username, rule=rule, name=name)
        elif 'rule' in session and session['rule'] == 'user':
            rule = session['rule']
            if 'name' in session:
                name = session['name']
            return render_template('user.html', username=username,rule=rule, name=name)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pengguna = MPengguna(username, password)
        if pengguna.authenticate():
            session['username'] = username
            session['rule'] = pengguna.userLevel()
            session['name'] = pengguna.accName()
            return redirect(url_for('index'))
        msg = 'Username/Password Salah!'
        return render_template('login.html',msg=msg)
    return render_template('login.html')

# ================TABEL ADMIN ==========================================================================================================
    # ==============SHOW TABEL MAHASISWA ==========================================================================================================
@app.route('/tabel')
def Admin():                        # Tabel admin
    pengguna = MPengguna()
    container = []
    container = pengguna.showAllM()
    return render_template('mahasiswa.html', container=container)
    # ================SHOW TABEL DETAIL PEMBAYARAN ======================================================================================================
@app.route('/Detail')
def Detail():
    pengguna = MPengguna()
    container = []
    container = pengguna.showAllDetail()
    return render_template('detail.html', container=container)
    # ================SHOW TABEL PEMBAYARAN ======================================================================================================
@app.route('/Payment')
def Payment():
	model = MPengguna()
	container = []
	container = model.selectDBPay()
	return render_template('pembayaran.html', container=container)
    # ================SHOW TABEL AKUN ============================================================================================================
@app.route('/accounts')
def accManage():
    pengguna = MPengguna()
    container = []
    container = pengguna.showAllAcc()
    return render_template('akun.html', container=container)

# ============ EDIT TABEL =======================================================================================================

# ================= TABEL MAHASISWA =====================================================================================================

@app.route('/insert', methods=['GET', 'POST'])
def insert():
	if request.method == 'POST':
		id_account = request.form['id_account']
		nim = request.form['nim']
		nama = request.form['nama']
		alamat = request.form['alamat']
		tempat_lahir = request.form['tempat_lahir']
		tgl_lahir = request.form['tgl_lahir']
		jenis_kelamin = request.form['jenis_kelamin']
		agama = request.form['agama']
		prodi = request.form['prodi']
		fakultas = request.form['fakultas']
		semester = request.form['semester']
		angkatan = request.form['angkatan']
		data = (id_account, nim, nama, alamat, tempat_lahir, tgl_lahir, jenis_kelamin, agama, prodi, fakultas, semester, angkatan)
		model = MPengguna()
		model.insertDB(data)
		return redirect(url_for('Admin'))
	else:
		return render_template('insert_mahasiswa.html')

@app.route('/update/<id_account>')
def update(id_account):
	model = MPengguna()
	data = model.getDBbyID(id_account)
	return render_template('update_mahasiswa.html', data= data)

@app.route('/update_process', methods=['GET', 'POST'])
def update_process():
	id_account = request.form['id_account']
	nim = request.form['nim']
	nama = request.form['nama']
	alamat = request.form['alamat']
	tempat_lahir = request.form['tempat_lahir']
	tgl_lahir = request.form['tgl_lahir']
	jenis_kelamin = request.form['jenis_kelamin']
	agama = request.form['agama']
	prodi = request.form['prodi']
	fakultas = request.form['fakultas']
	semester = request.form['semester']
	angkatan = request.form['angkatan']
	data = (nim, nama, alamat, tempat_lahir, tgl_lahir, jenis_kelamin, agama, prodi, fakultas, semester, angkatan, id_account)
	model = MPengguna()
	model.updateDB(data)
	return redirect(url_for('Admin'))

@app.route('/delete/<id_account>')
def delete(id_account):
	model = MPengguna()
	model.deleteDB(id_account)
	return redirect(url_for('Admin'))

    # =================== TABEL DETAIL ========================================================================================================

@app.route('/insert_detail', methods=['GET', 'POST'])
def insertDetail():
	if request.method == 'POST':
		id_biaya = request.form['id_biaya']
		Semester = request.form['Semester']
		Sumbangan = request.form['Sumbangan']
		Pra_Kuliah = request.form['Pra_Kuliah']
		her_registrasi = request.form['Her_Registrasion']
		SPP_Tetap = request.form['SPP_Tetap']
		SPP_Variable = request.form['SPP_Variable']
		UTS = request.form['UTS']
		UAS = request.form['UAS']
		total_biaya = request.form['Total']
		data = (id_biaya,Semester,Sumbangan,Pra_Kuliah,her_registrasi,SPP_Tetap,SPP_Variable,UTS,UAS,total_biaya)
		model = MPengguna()
		model.insertDBDetail(data)
		return redirect(url_for('Detail'))
	else:
		return render_template('insert_detail.html')

@app.route('/update_detail/<id_detail>')
def updateDetail(id_detail):
	model = MPengguna()
	data = model.getDBbyNoDetail(id_detail)
	return render_template('update_detail.html', data=data)

@app.route('/update_process_detail', methods=['GET','POST'])
def update_processDetail():
	Id_Detail = request.form['Id_Detail']
	Id_Biaya = request.form['Id_Biaya']
	Semester = request.form['Semester']
	Sumbangan = request.form['Sumbangan']
	Pra_Kuliah = request.form['Pra_Kuliah']
	her_registrasi = request.form['her_registrasi']
	SPP_Tetap = request.form['SPP_Tetap']
	SPP_Variable = request.form['SPP_Variable']
	UTS = request.form['UTS']
	UAS = request.form['UAS']
	total_biaya = request.form['total_biaya']
	data = (Id_Biaya,Semester,Sumbangan,Pra_Kuliah,her_registrasi,SPP_Tetap,SPP_Variable,UTS,UAS,total_biaya,Id_Detail)
	model = MPengguna()
	model.updateDBDetail(data)
	return redirect(url_for('Detail'))

@app.route('/delete_detail/<id_detail>')
def deleteDetail(id_detail):
	model = MPengguna()
	model.deleteDBDetail(id_detail)
	return redirect(url_for('index'))

	# =========================================TABEL PEMBAYARAN=============================================================
		
@app.route('/insert_pay', methods=['GET', 'POST'])
def insert_pay():
	if request.method == 'POST':
		tanggal = request.form['tanggal']
		nim = request.form['nim']
		nama = request.form['nama']
		prodi = request.form['prodi']
		semester = request.form['semester']
		id_biaya = request.form['id_biaya']
		jml_pembayaran = request.form['jml_pembayaran']
		jenis_pembayaran = request.form['jenis_pembayaran']
		data = (tanggal, nim, nama, prodi, semester, id_biaya, jml_pembayaran, jenis_pembayaran)
		model = MPengguna()
		model.insertDBPay(data)
		return redirect(url_for('Payment'))
	else:
		return render_template('insert_pembayaran.html')
		
@app.route('/update_pembayaran/<no>')
def update_pay(no):
	model = MPengguna()
	data = model.getDBbyNoPay(no)
	return render_template('update_pembayaran.html', data= data)
	
@app.route('/update_process_pay', methods=['GET', 'POST'])
def update_process_pay():
	id_pembayaran = request.form['id_pembayaran']
	tanggal = request.form['tanggal']
	nim = request.form['nim']
	nama = request.form['nama']
	prodi = request.form['prodi']
	semester = request.form['semester']
	id_biaya = request.form['id_biaya']
	jml_pembayaran = request.form['jml_pembayaran']
	jenis_pembayaran = request.form['jenis_pembayaran']
	data = (tanggal,nim, nama, prodi, semester, id_biaya, jml_pembayaran, jenis_pembayaran, id_pembayaran)
	model = MPengguna()
	model.updateDBPay(data)
	return redirect(url_for('Payment'))
	
@app.route('/delete_pay/<no>')
def delete_pay(no):
	model = MPengguna()
	model.deleteDBPay(no)
	return redirect(url_for('Payment'))

    # ================= TABEL AKUN =======================================================================================

@app.route('/insert_acc', methods=['GET', 'POST'])
def insert_acc():
	if request.method == 'POST':
		id_account = request.form['id_account']
		name = request.form['name']
		username = request.form['username']
		password = request.form['password']
		rule = request.form['rule']
		data = (id_account, name, username, password, rule)
		model = MPengguna()
		model.insertDBAcc(data)
		return redirect(url_for('accManage'))
	else:
		return render_template('insert_akun.html')

@app.route('/update_acc/<id_account>')
def update_acc(id_account):
	model = MPengguna()
	data = model.getAccbyID(id_account)
	return render_template('update_akun.html', data= data)

@app.route('/update_process_acc', methods=['GET', 'POST'])
def update_process_acc():
    id_account = request.form['id_account']
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    rule = request.form['rule']
    data = (name, username, password, rule, id_account)
    model = MPengguna()
    model.updateDBAcc(data)
    return redirect(url_for('accManage'))

@app.route('/delete_acc/<id_account>')
def deleteAcc(id_account):
	model = MPengguna()
	model.deleteDBacc(id_account)
	return redirect(url_for('accManage'))

# ============= TABEL USER =========================================================================================================

@app.route('/tabel_mahasiswa')
def User():                         #
    pengguna = MPengguna()
    container = []
    container = pengguna.showDataM()
    return render_template('mahasiswa_user.html', container=container)

@app.route('/Detail_user')
def DetailUser():
    pengguna = MPengguna()
    container = []
    container = pengguna.showAllDetail()
    return render_template('detail_user.html', container=container)

@app.route('/PaymentUser')
def PaymentUser():
	model = MPengguna()
	container = []
	container = model.selectDBPayUser()
	return render_template('pembayaran_user.html', container=container)

# ============ logout ======================================================================================================

@app.route('/logout')
def logout():
    session.pop('username','')
    session.pop('rule','')
    session.pop('name','')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)