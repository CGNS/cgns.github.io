.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _BCPropertyFigure:

BCProperty Figure
=================

.. container:: fighead
     
   **BCProperty Node**
   
   (See :ref:`BC_t <BCFigure>`  figure)
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`WallFunction`      
      * -  Label:    
        -  :sidsref:`WallFunction_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0,1     
      * -  Child Nodes:     
        -  :ref:`WallFunction_t figure <WallFunctionFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`Area`      
      * -  Label:    
        -  :sidsref:`Area_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0,1     
      * -  Child Nodes:     
        -  :ref:`Area_t figure <AreaFigure>`  

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
        -  User defined     
      * -  Label:     
        -  :sidsref:`UserDefinedData_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  

.. last line
