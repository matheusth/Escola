
BEGIN;
CREATE TABLE "Escola"."Responsavel"(
  "id" INTEGER PRIMARY KEY NOT NULL,
  "nome" VARCHAR(65) NOT NULL,
  "telefone" VARCHAR(11) NOT NULL
);
CREATE TABLE "Escola"."AreaAtuacao"(
  "id" INTEGER PRIMARY KEY NOT NULL,
  "nome" VARCHAR(45) NOT NULL
);
CREATE TABLE "Escola"."Professor"(
  "registro" INTEGER PRIMARY KEY NOT NULL,
  "nome" VARCHAR(65) NOT NULL,
  "telefone" VARCHAR(11) NOT NULL,
  "email" VARCHAR(75) NOT NULL,
  "areaAtuacao" INTEGER NOT NULL,
  CONSTRAINT "fk_Professor_areaAtuacao1"
    FOREIGN KEY("areaAtuacao")
    REFERENCES "AreaAtuacao"("id")
);
CREATE INDEX "Escola"."Professor.fk_Professor_areaAtuacao1_idx" ON "Professor" ("areaAtuacao");
CREATE TABLE "Escola"."Turma"(
  "id" INTEGER PRIMARY KEY NOT NULL,
  "nome" VARCHAR(45) NOT NULL,
  "inicioEm" INTEGER NOT NULL,
  "curso" INTEGER NOT NULL,
  CONSTRAINT "fk_Turma_Cursos1"
    FOREIGN KEY("curso")
    REFERENCES "Curso"("id")
);
CREATE INDEX "Escola"."Turma.fk_Turma_Cursos1_idx" ON "Turma" ("curso");
CREATE TABLE "Escola"."Curso"(
  "id" INTEGER PRIMARY KEY NOT NULL,
  "nome" VARCHAR(40) NOT NULL,
  "cargaHoraria" INTEGER NOT NULL DEFAULT CHECK(cargaHoraria > 0),
  "coordenador" INTEGER NOT NULL CHECK("coordenador">=0),
  CONSTRAINT "fk_Cursos_Professor1"
    FOREIGN KEY("coordenador")
    REFERENCES "Professor"("registro")
);
CREATE INDEX "Escola"."Curso.fk_Cursos_Professor1_idx" ON "Curso" ("coordenador");
CREATE TABLE "Escola"."Aluno"(
  "matricula" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "nome" VARCHAR(65) NOT NULL,
  "email" VARCHAR(75) NOT NULL,
  "endereco" VARCHAR(85) NOT NULL,
  "turma" INTEGER NOT NULL,
  "responsavel" INTEGER NOT NULL,
  CONSTRAINT "fk_Aluno_Turma"
    FOREIGN KEY("turma")
    REFERENCES "Turma"("id"),
  CONSTRAINT "fk_Aluno_Resposavel1"
    FOREIGN KEY("turma")
    REFERENCES "Responsavel"("id")
);
CREATE INDEX "Escola"."Aluno.fk_Aluno_Turma_idx" ON "Aluno" ("turma");
COMMIT;
