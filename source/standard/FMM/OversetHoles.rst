.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _OversetHolesFigure:

OversetHoles Figure
===================

.. container:: fighead
     
   **OversetHoles Node**
   
   (See :ref:`ZoneGridConnectivity_t figure <ZoneGridConnectivityFigure>` )
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:     
        -  :sidsref:`Descriptor_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`PointRange`      
      * -  Label:     
        -  :sidsref:`IndexRange_t`      
      * -  See:    
        -  :ref:`GridConnectivity_t figure <GridConnectivityFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`PointList`      
      * -  Label:     
        -  :sidsref:`IndexArray_t`      
      * -  See:    
        -  :ref:`GridConnectivity_t figure <GridConnectivityFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`GridLocation`      
      * -  Label:     
        -  :sidsref:`GridLocation_t`      
      * -  See:    
        -  :ref:`FlowSolution_t figure <FlowSolutionFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:     
        -  :sidsref:`UserDefinedData_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  

.. note::

   The nodes :sidskey:`PointRange` and :sidskey:`PointList` are mutually exclusive. Use one format or the other. 


.. last line
