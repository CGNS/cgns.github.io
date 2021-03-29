.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _TurbulenceModelFigure:

TurbulenceModel Figure
======================

.. container:: fighead
     
   **TurbulenceModel Node**
   
   (See :ref:`FlowEquationSet_t figure <FlowEquationSetFigure>` )
   
     


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
        -  Data-name identifier or user defined     
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`DataType`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  1     
      * -  Data:    
        -  Data quantity     
      * -  Cardinality:    
        -  0, *N*      
      * -  Parameters:    
        -  :sidskey:`DataType`      
      * -  Child Nodes:    
        -  :ref:`DataArray_t figure <DataArrayFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidsref:`DiffusionModel`      
      * -  Label:     
        -  ":sidskey:`int[1 + ... + IndexDimension]` "     
      * -  See:    
        -  :ref:`GoverningEquations_t figure <GoverningEquationsFigure>`  

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

  #. The diffusion model as defined here is only applicable to structured zones.
  #. For a structured zone, :sidskey:`IndexDimension = CellDimension`. 

.. last line
