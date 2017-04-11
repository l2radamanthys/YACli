# YACli 
Yet Another Custom library

Interfaz personalizada para creacion de componentes para diferentes lenguajes.

## Uso

    python cli.py [componente] [nombre]

Donde:

- **componente:** es el nombre del componente que vamos a utilizar

- **nombre:** es el nombre que le damos y sera usado como archivo de salida, por lo general se recomienda escribirlo en _camel-case_.

## Componentes Disponibles

#### angular-component (*ng-c*)

Crea una carpeta con la siguiente extructura

    ./[nombre]
        [nombre].component.ts
		[nombre].component.html
		[nombre].css

**Nota:** _[nombre]_ combiene escribirlo con CamelCase ya que para nombre de archivos y carpetas sera convertido a notación pascal.

El componente generado corresponde a Angular.io o Angular2 no a AngularJs

#### angular-service (*ng-s*)

[#Todo] no hay documentacion disponible 

#### typescript-class (*ts-c*)

[#Todo] no hay documentacion disponible

#### angular-class

solo es un alias de **typescript-class**