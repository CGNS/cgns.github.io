.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _GridConnectivityPropertyFigure:

GridConnectivityProperty Figure
===============================

.. container:: fighead
     
   **GridConnectivityProperty Node**
   
   (See :ref:`GridConnectivity1to1_t <GridConnectivity1to1Figure>` :ref:`GridConnectivity_t <GridConnectivityFigure>` figures)
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`Periodic`      
      * -  Label:    
        -  :sidsref:`Periodic_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0,1     
      * -  Child Nodes:     
        -  :ref:`Periodic_t figure <PeriodicFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`AverageInterface`      
      * -  Label:    
        -  :sidsref:`AverageInterface_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0,1     
      * -  Child Nodes:     
        -  :ref:`AverageInterface_t figure <AverageInterfaceFigure>`  

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
