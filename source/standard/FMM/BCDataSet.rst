.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _BCDataSetFigure:

BCDataSet Figure
================

.. container:: fighead
     
   **BCDataSet Node**
   
   (See :ref:`BC_t <BCFigure>`  figure)
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`DirichletData`      
      * -  Label:    
        -  :sidsref:`BCData_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0,1     
      * -  Functions:    
        -  :sidsref:`ListLength`      
      * -  Child Nodes:     
        -  :ref:`BCData_t figure <BCDataFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`NeumannData`      
      * -  Label:    
        -  :sidsref:`BCData_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0,1     
      * -  Functions:    
        -  :sidsref:`ListLength`      
      * -  Child Nodes:     
        -  :ref:`BCData_t figure <BCDataFigure>`  

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
        -  :sidskey:`PointRange`      
      * -  Label:     
        -  :sidsref:`IndexRange_t`      
      * -  See:    
        -  :ref:`BC_t figure <BCFigure>`  

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
        -  :ref:`BC_t figure <BCFigure>`  

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
        -  :sidskey:`ReferenceState`      
      * -  Label:     
        -  :sidsref:`ReferenceState_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`DataClass`      
      * -  Label:     
        -  :sidsref:`DataClass_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`DimensionalUnits`      
      * -  Label:     
        -  :sidsref:`DimensionalUnits_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  

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

.. last line
