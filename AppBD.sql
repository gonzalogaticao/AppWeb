/*==============================================================*/
/* Table: MODERADORES                                           */
/*==============================================================*/
create table MODERADORES 
(
   ID_M                 integer                        not null   AUTO_INCREMENT,
   NOMBRE_M             varchar(50)                    null,
   CORREO_M             varchar(50)                    null,
   CONTRASENA_M         varchar(50)                    null,
   constraint PK_MODERADORES primary key (ID_M)
);

/*==============================================================*/
/* Index: MODERADORES_PK                                        */
/*==============================================================*/
create unique index MODERADORES_PK on MODERADORES (
ID_M ASC
);

/*==============================================================*/
/* Table: TESIS                                                 */
/*==============================================================*/
create table TESIS 
(
   ID_T                 integer                        not null   AUTO_INCREMENT,
   ID_M                 integer                        not null,
   ID_U                 integer                        not null,
   TITULO_T             char(50)                       null,
   AUTORES_T            char(200)                      null,
   PROFESOR_T           char(50)                       null,
   ANIO_T               integer                        null,
   ARCHIVO_T            char(10)                       null,
   constraint PK_TESIS primary key (ID_T)
);

/*==============================================================*/
/* Index: TESIS_PK                                              */
/*==============================================================*/
create unique index TESIS_PK on TESIS (
ID_T ASC
);

/*==============================================================*/
/* Index: MODERAR_FK                                            */
/*==============================================================*/
create index MODERAR_FK on TESIS (
ID_M ASC
);

/*==============================================================*/
/* Index: PUBLICAR_FK                                           */
/*==============================================================*/
create index PUBLICAR_FK on TESIS (
ID_U ASC
);

/*==============================================================*/
/* Table: USUARIOS                                              */
/*==============================================================*/
create table USUARIOS 
(
   ID_U                 integer                        not null   AUTO_INCREMENT,
   CORREO_U             varchar(50)                    null,
   CONTRASENA_U         varchar(50)                    null,
   constraint PK_USUARIOS primary key (ID_U)
);

/*==============================================================*/
/* Index: USUARIOS_PK                                           */
/*==============================================================*/
create unique index USUARIOS_PK on USUARIOS (
ID_U ASC
);

alter table TESIS
   add constraint FK_TESIS_MODERAR_MODERADO foreign key (ID_M)
      references MODERADORES (ID_M)
      on update restrict
      on delete restrict;

alter table TESIS
   add constraint FK_TESIS_PUBLICAR_USUARIOS foreign key (ID_U)
      references USUARIOS (ID_U)
      on update restrict
      on delete restrict;

