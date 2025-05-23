.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _ZoneIterativeDataFigure:

.. _ParticleIterativeDataFigure:

ZoneIterativeData/ParticleIterativeData Figure
==============================================

.. container:: fighead
     
   **ZoneIterativeData or ParticleIterativeData Node**
   
   (See :ref:`Zone_t figure <ZoneFigure>` or :ref:`ParticleZone_t figure <ParticleZoneFigure>`)
   
     


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
        -  :sidskey:`C1`  or user defined     
      * -  Dimensions:    
        -  2 or user defined     
      * -  Dimension Values:     
        -  (32, :sidskey:`NumberOfSteps` ) or user defined     
      * -  Data:    
        -  Context dependent or user defined     
      * -  Cardinality:    
        -  0, *N*      
      * -  Parameters:    
        -  :sidskey:`DataType` , dimension of data, size of data     
      * -  Child Nodes:    
        -  :ref:`DataArray_t figure <DataArrayFigure>`  

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
        -  User defined     
      * -  Label:     
        -  :sidsref:`UserDefinedData_t`      
      * -  See:    
        -  :ref:`UserDefinedData_t figure <UserDefinedDataFigure>`  

.. last line
