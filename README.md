**SIGNAL CHAIN**

**Instalacion**
---

1) PC desde cero

$ sudo apt-get install python-pip gfortran libpng-dev libblas-dev liblapack-dev libatlas-base-dev  python-tk libssl-dev libhdf5-dev

2) Instalar Anaconda

3) Crear un entorno de desarrollo

$ conda create --name=schain_master python=3.10

4) Activar el entorno

$ conda activate schain_master

5) Clonar el repositorio

$ git clone http://jro-dev.igp.gob.pe/rhodecode/schain


6) Moverse si es necesario a la rama del repositorio de interes.


$ cd schain

$ git checkout v3.0-devel # si queremos movernos a otra rama v3.0-devel

$ cd schainpy

$ pip install numpy

$ pip install ./

$ pip install mako

$ pip install packaging

$ cd ..


7) Instalar digital_rf

$ git clone https://github.com/MITHaystack/digital_rf

$ cd digital_rf

$ mkdir build 

$ cd build

$ cmake ..

$ make

$ sudo make install

$ sudo ldconfig

