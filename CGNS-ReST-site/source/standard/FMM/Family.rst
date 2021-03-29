.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _FamilyFigure:

Family Figure
=============

.. container:: fighead
     
   **Family Node**
   
   (See :ref:`CGNSBase_t figure <CGNSBaseFigure>` )
   
     


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
        -  :sidskey:`Ordinal`      
      * -  Label:     
        -  :sidsref:`Ordinal_t`      
      * -  See:    
        -  :ref:`Zone_t figure <ZoneFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:    
        -  :sidsref:`Family_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0,N     
      * -  Child Nodes:     
        -  :ref:`Family_t figure <FamilyFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:    
        -  :sidsref:`FamilyBC_t`      
      * -  Data-Type:    
        -  :sidskey:`C1`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  Length of string     
      * -  Data:    
        -  :sidskey:`BCType`  value     
      * -  Cardinality:    
        -  0,1     
      * -  Child Nodes:     
        -  :ref:`FamilyBC_t figure <FamilyBCFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:    
        -  :sidskey:`FamilyName_t` `      
      * -  Data-Type:    
        -  :sidskey:`C1`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  Length of string     
      * -  Data:    
        -  Family name     
      * -  Cardinality:    
        -  0,N 

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:    
        -  :sidsref:`GeometryReference_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0, *N*      
      * -  Child Nodes:     
        -  :ref:`GeometryReference_t figure <GeometryReferenceFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`RotatingCoordinates`      
      * -  Label:     
        -  :sidsref:`RotatingCoordinates_t`      
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
