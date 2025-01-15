#!/usr/bin/python

from schainpy.controller import Project

controller = Project()
controller.setup(id = '100', 
                 name='test', 
                 description='Basic experiment')

path="/home/soporte/Documents/CHARLA_SCHAIN/Schain_presentacion/data"

read_unit = controller.addReadUnit(datatype='Spectra',
                                   path=path,
                                   startDate='2012/01/31',
                                   endDate='2020/12/31',
                                   startTime='00:00:00',
                                   endTime='23:59:59',
                                   online=0,                         
                                   walk=0)

proc_unit = controller.addProcUnit(datatype='Spectra', 
                                   inputId=read_unit.getId())

op = proc_unit.addOperation(name='selectChannels')
op.addParameter(name='channelList', value='0,1', format='intlist')

op = proc_unit.addOperation(name='selectHeights')
op.addParameter(name='minHei', value='80', format='float')
op.addParameter(name='maxHei', value='200', format='float')

op = proc_unit.addOperation(name='removeDC')

op = proc_unit.addOperation(name='SpectraPlot')
op.addParameter(name='id', value='1', format='int')
op.addParameter(name='wintitle', value='Spectra', format='str')

op = proc_unit.addOperation(name='RTIPlot', optype='other')
op.addParameter(name='id', value='2', format='int')
op.addParameter(name='wintitle', value='RTI', format='str')

controller.start()


