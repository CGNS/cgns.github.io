.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _ReferenceStateFigure:

ReferenceState Figure
=====================

.. container:: fighead
     
   **ReferenceState Node**
   
   (See :ref:`CGNSBase_t <CGNSBaseFigure>`  and :ref:`Zone_t <ZoneFigure>`  figures)
   
     


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
        -  Reference state data     
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
        -  :sidsref:`ReferenceStateDescription`      
      * -  Label:    
        -  :sidsref:`Descriptor_t`      
      * -  Data-Type:    
        -  :sidskey:`C1`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  Length of string     
      * -  Data:    
        -  Description of data     
      * -  Cardinality:    
        -  0,1 

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
