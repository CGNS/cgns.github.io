.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _GeometryReferenceFigure:

GeometryReference Figure
========================

.. container:: fighead
     
   **GeometryReference Node**
   
   (See :ref:`Family_t figure <FamilyFigure>` )
   
     


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
        -  :sidskey:`GeometryFile`      
      * -  Label:    
        -  :sidsref:`GeometryFile_t`      
      * -  Data-Type:    
        -  :sidskey:`C1`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  Length of string     
      * -  Data:    
        -  Name of the geometry file     
      * -  Cardinality:    
        -  1 

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`GeometryFormat`      
      * -  Label:    
        -  :sidsref:`GeometryFormat_t`      
      * -  Data-Type:    
        -  :sidskey:`C1`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  Length of string     
      * -  Data:    
        -  Name of the geometry format     
      * -  Cardinality:    
        -  1 

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:    
        -  :sidsref:`GeometryEntity_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:     
        -  0, *N*  

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
