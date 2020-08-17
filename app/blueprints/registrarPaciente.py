from flask import Blueprint, render_template, redirect, request, url_for
from datetime import datetime
from dao.paciente import removePaciente, updatePaciente, savePaciente, selectPaciente
from flask_login import login_required, current_user
import forms.inputs as inputs
from blueprints.login import ler_dados

registrarPaciente = Blueprint('Paciente', __name__)

@registrarPaciente.route('/paciente', methods=['GET', 'POST'])
@login_required 
def registrar():

    if not (current_user.perfil == 'master' or current_user.perfil == 'admin'):
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':

        nome = request.form['nome']
        cpf = request.form['cpf']
        cns = request.form['cns']
        id_genero = request.form['id_genero']
        id_etnia = request.form['id_etnia']
        dataNasc = datetime.strptime(request.form['data_nasc'], '%d/%m/%Y').date() if len(request.form['data_nasc']) != 0 else None
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        savePaciente(nome, cpf, cns, telefone, dataNasc, id_etnia, id_genero, endereco, current_user.id_cidade)

        return redirect(url_for('admin.admin'))
    
    fields = {
        "nome" :inputs.nome,
        "cpf" : inputs.cpf,
        "cns" : inputs.cns,
        "genero" : inputs.genero,
        "etnia" : inputs.etnia,
        "dataNasc" : inputs.data_nasc,
        "endereco" : inputs.endereco,
        "telefone" : inputs.telefone
    }
    return render_template('paciente.html', dados = ler_dados(), fields = fields, master=(current_user.perfil == 'master'))

@registrarPaciente.route('/paciente/remove', methods=['GET', 'POST'])
@login_required 
def remove():
    if not (current_user.perfil == 'master' or current_user.perfil == 'admin'):
        return redirect(url_for('MenuAtendente.index'))
    
    
    if request.method == 'POST':
        id = request.form['paciente_id']

        removePaciente(id)

    return redirect(url_for('admin.admin'))

@registrarPaciente.route('/paciente/update', methods=['GET', 'POST'])
@login_required 
def update():

    if not (current_user.perfil == 'master' or current_user.perfil == 'admin'):
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':
        id = request.form['paciente_id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        cns = request.form['cns']
        id_genero = request.form['id_genero']
        id_etnia = request.form['id_etnia']
        dataNasc = datetime.strptime(request.form['data_nasc'], '%d/%m/%Y').date() if len(request.form['data_nasc']) != 0 else None
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        #print(dataNasc)

        updatePaciente(id, nome, cpf, cns, telefone, id_etnia, id_genero, dataNasc, endereco)    

    return redirect(url_for('admin.admin'))