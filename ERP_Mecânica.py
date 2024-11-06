# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ERP_Mecânica.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

### Import Telas Sistema ###

from Clientes import Ui_formCliente


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imgBackground = QtWidgets.QLabel(self.centralwidget)
        self.imgBackground.setGeometry(QtCore.QRect(-250, 70, 1131, 201))
        self.imgBackground.setStyleSheet("image: url(:/logo_empresa/icons/icon_erp.png)")
        self.imgBackground.setText("")
        self.imgBackground.setObjectName("imgBackground")
        self.bt_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.bt_cliente.setGeometry(QtCore.QRect(0, 0, 81, 71))
        self.bt_cliente.setStyleSheet("image: url(:/icon_cliente/icons/cliente.png)")
        self.bt_cliente.setText("")
        self.bt_cliente.setObjectName("bt_cliente")
        self.bt_fornecedor = QtWidgets.QPushButton(self.centralwidget)
        self.bt_fornecedor.setGeometry(QtCore.QRect(80, 0, 81, 71))
        self.bt_fornecedor.setStyleSheet("image: url(:/icon_fornecedor/icons/fornecedor.png)")
        self.bt_fornecedor.setText("")
        self.bt_fornecedor.setObjectName("bt_fornecedor")
        self.bt_produtos = QtWidgets.QPushButton(self.centralwidget)
        self.bt_produtos.setGeometry(QtCore.QRect(160, 0, 81, 71))
        self.bt_produtos.setStyleSheet("image: url(:/icon_produtos/icons/produtos.png)")
        self.bt_produtos.setText("")
        self.bt_produtos.setObjectName("bt_produtos")
        self.bt_vendas = QtWidgets.QPushButton(self.centralwidget)
        self.bt_vendas.setGeometry(QtCore.QRect(240, 0, 81, 71))
        self.bt_vendas.setStyleSheet("image:url(:/icon_venda/icons/venda.png)")
        self.bt_vendas.setText("")
        self.bt_vendas.setObjectName("bt_vendas")
        self.bt_pagar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_pagar.setGeometry(QtCore.QRect(320, 0, 81, 71))
        self.bt_pagar.setStyleSheet("image:url(:/icon_pagar/icons/contasPagar.png)")
        self.bt_pagar.setText("")
        self.bt_pagar.setObjectName("bt_pagar")
        self.bt_receber = QtWidgets.QPushButton(self.centralwidget)
        self.bt_receber.setGeometry(QtCore.QRect(400, 0, 81, 71))
        self.bt_receber.setStyleSheet("image: url(:/icon_receber/icons/receber.png)")
        self.bt_receber.setText("")
        self.bt_receber.setObjectName("bt_receber")
        self.bt_caixa = QtWidgets.QPushButton(self.centralwidget)
        self.bt_caixa.setGeometry(QtCore.QRect(480, 0, 81, 71))
        self.bt_caixa.setStyleSheet("image: url(:/icon_caixa/icons/caixa.png)")
        self.bt_caixa.setText("")
        self.bt_caixa.setObjectName("bt_caixa")
        self.bt_sair = QtWidgets.QPushButton(self.centralwidget)
        self.bt_sair.setGeometry(QtCore.QRect(560, 0, 81, 71))
        self.bt_sair.setStyleSheet("image: url(:/icon_sair/icons/sair.png)")
        self.bt_sair.setText("")
        self.bt_sair.setObjectName("bt_sair")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastros = QtWidgets.QMenu(self.menubar)
        self.menuCadastros.setObjectName("menuCadastros")
        self.menuOperacoes = QtWidgets.QMenu(self.menubar)
        self.menuOperacoes.setObjectName("menuOperacoes")
        self.menuSa_da_de_Produtos = QtWidgets.QMenu(self.menuOperacoes)
        self.menuSa_da_de_Produtos.setObjectName("menuSa_da_de_Produtos")
        self.menuEstoque = QtWidgets.QMenu(self.menuOperacoes)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuCompras = QtWidgets.QMenu(self.menuOperacoes)
        self.menuCompras.setObjectName("menuCompras")
        self.menuFinanceiro = QtWidgets.QMenu(self.menubar)
        self.menuFinanceiro.setObjectName("menuFinanceiro")
        self.menuConsultas = QtWidgets.QMenu(self.menubar)
        self.menuConsultas.setObjectName("menuConsultas")
        self.menuVendas = QtWidgets.QMenu(self.menuConsultas)
        self.menuVendas.setObjectName("menuVendas")
        self.menuConsumos = QtWidgets.QMenu(self.menuConsultas)
        self.menuConsumos.setObjectName("menuConsumos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCliente = QtWidgets.QAction(MainWindow)
        self.actionCliente.setObjectName("actionCliente")
        self.actionFornecedor = QtWidgets.QAction(MainWindow)
        self.actionFornecedor.setObjectName("actionFornecedor")
        self.actionUsuarios = QtWidgets.QAction(MainWindow)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.actionVenda = QtWidgets.QAction(MainWindow)
        self.actionVenda.setObjectName("actionVenda")
        self.actionConsumo = QtWidgets.QAction(MainWindow)
        self.actionConsumo.setObjectName("actionConsumo")
        self.actionSaldo = QtWidgets.QAction(MainWindow)
        self.actionSaldo.setObjectName("actionSaldo")
        self.actionCompras_2 = QtWidgets.QAction(MainWindow)
        self.actionCompras_2.setObjectName("actionCompras_2")
        self.actionPedido = QtWidgets.QAction(MainWindow)
        self.actionPedido.setObjectName("actionPedido")
        self.actionCancelar = QtWidgets.QAction(MainWindow)
        self.actionCancelar.setObjectName("actionCancelar")
        self.actionCaixa = QtWidgets.QAction(MainWindow)
        self.actionCaixa.setObjectName("actionCaixa")
        self.actionContas_Bancos = QtWidgets.QAction(MainWindow)
        self.actionContas_Bancos.setObjectName("actionContas_Bancos")
        self.actionContas_p_pagar = QtWidgets.QAction(MainWindow)
        self.actionContas_p_pagar.setObjectName("actionContas_p_pagar")
        self.actionContas_pagas = QtWidgets.QAction(MainWindow)
        self.actionContas_pagas.setObjectName("actionContas_pagas")
        self.actionContas_p_receber = QtWidgets.QAction(MainWindow)
        self.actionContas_p_receber.setObjectName("actionContas_p_receber")
        self.actionContas_recebidas = QtWidgets.QAction(MainWindow)
        self.actionContas_recebidas.setObjectName("actionContas_recebidas")
        self.actionGeral = QtWidgets.QAction(MainWindow)
        self.actionGeral.setObjectName("actionGeral")
        self.actionResumo = QtWidgets.QAction(MainWindow)
        self.actionResumo.setObjectName("actionResumo")
        self.actionGeral_2 = QtWidgets.QAction(MainWindow)
        self.actionGeral_2.setObjectName("actionGeral_2")
        self.actionResumo_2 = QtWidgets.QAction(MainWindow)
        self.actionResumo_2.setObjectName("actionResumo_2")
        self.menuCadastros.addSeparator()
        self.menuCadastros.addAction(self.actionCliente)
        self.menuCadastros.addAction(self.actionFornecedor)
        self.menuCadastros.addAction(self.actionUsuarios)
        self.menuSa_da_de_Produtos.addAction(self.actionVenda)
        self.menuSa_da_de_Produtos.addAction(self.actionConsumo)
        self.menuEstoque.addAction(self.actionSaldo)
        self.menuCompras.addAction(self.actionCompras_2)
        self.menuCompras.addAction(self.actionPedido)
        self.menuCompras.addAction(self.actionCancelar)
        self.menuOperacoes.addAction(self.menuSa_da_de_Produtos.menuAction())
        self.menuOperacoes.addAction(self.menuEstoque.menuAction())
        self.menuOperacoes.addAction(self.menuCompras.menuAction())
        self.menuFinanceiro.addAction(self.actionCaixa)
        self.menuFinanceiro.addAction(self.actionContas_Bancos)
        self.menuFinanceiro.addAction(self.actionContas_p_pagar)
        self.menuFinanceiro.addAction(self.actionContas_pagas)
        self.menuFinanceiro.addAction(self.actionContas_p_receber)
        self.menuFinanceiro.addAction(self.actionContas_recebidas)
        self.menuVendas.addAction(self.actionGeral)
        self.menuVendas.addAction(self.actionResumo)
        self.menuConsumos.addAction(self.actionGeral_2)
        self.menuConsumos.addAction(self.actionResumo_2)
        self.menuConsultas.addAction(self.menuVendas.menuAction())
        self.menuConsultas.addAction(self.menuConsumos.menuAction())
        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuOperacoes.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())
        self.menubar.addAction(self.menuConsultas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuCadastros.setTitle(_translate("MainWindow", "Cadastros"))
        self.menuOperacoes.setTitle(_translate("MainWindow", "Operacoes"))
        self.menuSa_da_de_Produtos.setTitle(_translate("MainWindow", "Saída de Produtos"))
        self.menuEstoque.setTitle(_translate("MainWindow", "Estoque"))
        self.menuCompras.setTitle(_translate("MainWindow", "Compras"))
        self.menuFinanceiro.setTitle(_translate("MainWindow", "Financeiro"))
        self.menuConsultas.setTitle(_translate("MainWindow", "Consultas"))
        self.menuVendas.setTitle(_translate("MainWindow", "Vendas"))
        self.menuConsumos.setTitle(_translate("MainWindow", "Consumos"))
        self.actionCliente.setText(_translate("MainWindow", "Cliente"))
        self.actionFornecedor.setText(_translate("MainWindow", "Fornecedor"))
        self.actionUsuarios.setText(_translate("MainWindow", "Usuarios"))
        self.actionVenda.setText(_translate("MainWindow", "Venda"))
        self.actionConsumo.setText(_translate("MainWindow", "Consumo"))
        self.actionSaldo.setText(_translate("MainWindow", "Saldo"))
        self.actionCompras_2.setText(_translate("MainWindow", "Comprar"))
        self.actionPedido.setText(_translate("MainWindow", "Pedido"))
        self.actionCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.actionCaixa.setText(_translate("MainWindow", "Caixa"))
        self.actionContas_Bancos.setText(_translate("MainWindow", "Contas Bancos"))
        self.actionContas_p_pagar.setText(_translate("MainWindow", "Contas p/ pagar"))
        self.actionContas_pagas.setText(_translate("MainWindow", "Contas pagas"))
        self.actionContas_p_receber.setText(_translate("MainWindow", "Contas p/ receber"))
        self.actionContas_recebidas.setText(_translate("MainWindow", "Contas recebidas"))
        self.actionGeral.setText(_translate("MainWindow", "Geral"))
        self.actionResumo.setText(_translate("MainWindow", "Resumo"))
        self.actionGeral_2.setText(_translate("MainWindow", "Geral"))
        self.actionResumo_2.setText(_translate("MainWindow", "Resumo"))
        
        
        ### BOTÕES SISTEMA ###
        self.bt_sair.clicked.connect(self.sairSistema) # Fecha o sistema
        self.bt_cliente.clicked.connect(self.telaCliente) # Abre tela Cliente
        self.actionCliente.triggered.connect(self.telaCliente) # Abre tela Cliente
        
    ### FUNÇÕES SISTEMA ###
    ## FECHAR SISTEMA ##
    def sairSistema(self):
        sys.exit()
        
    ## ABRE TELACLIENTE ##
    def telaCliente(self):
        self.formCliente = QtWidgets.QWidget()
        self.ui = Ui_formCliente()
        self.ui.setupUi(self.formCliente)
        self.formCliente.show()
        
#### Imagens Sistema ###
import icon_caixa
import icon_cliente
import icon_fornecedor
import icon_pagar
import icon_produtos
import icon_receber
import icon_sair
import icon_vendas
import logo_empresa


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
