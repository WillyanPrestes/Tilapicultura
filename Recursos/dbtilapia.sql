create database dbtilapicultura;
use dbtilapicultura;

CREATE TABLE EstadoFederal (
    IdEstado varchar(2) NOT NULL,
    Uf varchar(2) NOT NULL,
    Nome varchar(60) NOT NULL,
    PRIMARY KEY (IdEstado)
);

CREATE TABLE Municipio (
    IdMunicipio varchar(8) NOT NULL,
    Nome varchar(120) NOT NULL,
    IdEstado varchar(2) NOT NULL,
    PRIMARY KEY (IdMunicipio),
    CONSTRAINT FK_Municipio_EstadoFederal_IdEstado FOREIGN KEY (IdEstado) REFERENCES EstadoFederal (IdEstado) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Endereco (
	IdEndereco int UNSIGNED NOT NULL AUTO_INCREMENT,
    IdMunicipio varchar(8) NOT NULL,
    Logradouro varchar(120) NOT NULL,
    Bairro varchar(100) NOT NULL,
    Numero int NOT NULL,
    Cep int NOT NULL,
    PRIMARY KEY (IdEndereco),
    CONSTRAINT  FK_Endereco_Municipio_IdMunicipio  FOREIGN KEY (IdMunicipio)
    REFERENCES  Municipio(IdMunicipio) ON DELETE  RESTRICT
);


CREATE TABLE IF NOT EXISTS Pessoa (
    IdPessoa int UNSIGNED NOT NULL AUTO_INCREMENT,
    IdEndereco int UNSIGNED NOT NULL,
    Nome varchar(120) NOT NULL,
    Apelido varchar(120),
    RG varchar(8),
    CPF varchar(14),
    RazaoSocial varchar(120) NOT NULL,
    NomeFantasia varchar(120),
    Cnpj varchar(14),
    InscricaoEstadual varchar(20),
	tipoObjeto int,
    PRIMARY KEY (IdPessoa),
    CONSTRAINT  FK_Pessoa_Endereco_IdEndereco FOREIGN KEY (IdEndereco)
    REFERENCES  Endereco(IdEndereco) ON DELETE  RESTRICT
);


CREATE TABLE IF NOT EXISTS Fornecedor (
    IdPessoa int UNSIGNED NOT NULL,
    IdFornecedor int UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (IdFornecedor),
    CONSTRAINT  FK_Fornecedor_Pessoa_IdFornecedor  FOREIGN KEY (IdPessoa)
    REFERENCES  Pessoa(IdPessoa) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Item (
    IdItem int UNSIGNED NOT NULL AUTO_INCREMENT,
    Descricao varchar(180) NOT NULL,
    Qtd int NOT NULL,
    Preco decimal(18,2) NOT NULL,
    PRIMARY KEY (IdItem)
);

CREATE TABLE IF NOT EXISTS Alimentos (
	IdItem int UNSIGNED NOT NULL,
    Kilo decimal(18,2) NOT NULL,
    PRIMARY KEY (IdItem),
    CONSTRAINT  FK_Alimentos_Item_IdItem  FOREIGN KEY (IdItem)
    REFERENCES  Item(IdItem) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Compra (
    IdCompra int UNSIGNED NOT NULL AUTO_INCREMENT,
    IdFornecedor int UNSIGNED NOT NULL,
    ValorTotal decimal(18,2) NOT NULL,
    DataHora datetime NOT NULL,
    PRIMARY KEY (IdCompra),
    CONSTRAINT  FK_Compra_Fornecedor_IdFornecedor  FOREIGN KEY (IdFornecedor)
    REFERENCES  Fornecedor(IdFornecedor) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS CompraItem (
    IdCompra int UNSIGNED NOT NULL,
    IdItem int UNSIGNED NOT NULL,
    Valor decimal(18,2) NOT NULL,
    Qtd int NOT NULL,
    PRIMARY KEY (IdCompra,IdItem),
    CONSTRAINT  FK_Compra_CompraItem_IdCompra  FOREIGN KEY (IdCompra)
    REFERENCES  Compra(IdCompra) ON DELETE  RESTRICT,
    CONSTRAINT  FK_CompraItem_Item_IdItem FOREIGN KEY (IdItem)
    REFERENCES Item(IdItem) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS AjusteItem (
    IdAjuste int UNSIGNED NOT NULL AUTO_INCREMENT,
    IdItem int UNSIGNED NOT NULL,
    Descricao varchar(200) NOT NULL,
    Qtd int NOT NULL,
    DataHora datetime NOT NULL,
    PRIMARY KEY (IdAjuste),
    CONSTRAINT  FK_AjusteItem_Item_IdItem FOREIGN KEY (IdItem)
    REFERENCES Item(IdItem) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Tanques (
    IdTanque int UNSIGNED NOT NULL AUTO_INCREMENT,
    Descricao varchar(200),
    QtdPeixe int NOT NULL,
    PH int NOT NULL,
    Temperatura decimal(3,2) NOT NULL,
    Volume decimal(18,2) NOT NULL,
    FaseDesenvolvimento int NOT NULL,
    PRIMARY KEY (IdTanque)
);

CREATE TABLE IF NOT EXISTS HorarioAlimentacao (
    IdHorario int UNSIGNED NOT NULL AUTO_INCREMENT,
    IdTanque int UNSIGNED NOT NULL,
    Hora datetime NOT NULL,
    Kilo decimal(18,2) NOT NULL,
    IdItem int UNSIGNED NOT NULL,
    PRIMARY KEY (IdHorario),
    CONSTRAINT FK_HorarioAlimentacao_Alimentos_IdItem  FOREIGN KEY (IdItem)
    REFERENCES Alimentos(IdItem) ON DELETE RESTRICT,
    CONSTRAINT FK_HorarioAlimentacao_Tanques_IdTanque FOREIGN KEY (IdTanque)
    REFERENCES Tanques(IdTanque) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Colheita (
    IdColheita int UNSIGNED NOT NULL AUTO_INCREMENT,
    DataColheita datetime NOT NULL,
    Qtd int NOT NULL,
    PesoMedio decimal(18,2) NOT NULL,
    IdTanque int UNSIGNED NOT NULL,
    PRIMARY KEY (IdColheita),
    CONSTRAINT FK_Colheita_Tanques_IdTanque FOREIGN KEY (IdTanque)
    REFERENCES Tanques(IdTanque) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS AjusteTanque (
	IdAjusteEstoque int UNSIGNED NOT NULL AUTO_INCREMENT,
    IdTanque int UNSIGNED NOT NULL,
    QtdAtual int NOT NULL,
    QtdMovimentacao int NOT NULL,
    QtdNova int NOT NULL,
    Descricao varchar(200),
    PRIMARY KEY (IdAjusteEstoque),
    CONSTRAINT  FK_AjusteTanque_Tanques_IdTanque FOREIGN KEY (IdTanque)
    REFERENCES Tanques(IdTanque) ON DELETE RESTRICT
);












