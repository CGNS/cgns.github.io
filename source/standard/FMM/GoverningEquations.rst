.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _GoverningEquationsFigure:

GoverningEquations Figure
=========================

.. container:: fighead
     
   **GoverningEquations Node**
   
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
        -  :sidsref:`DiffusionModel`      
      * -  Label:    
        -  ":sidskey:`int[1 + ... + IndexDimension]` "     
      * -  Data-Type:    
        -  :sidskey:`I4`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  f(:sidskey:`IndexDimension` )     
      * -  Data:    
        -  Diffusion term indices     
      * -  Cardinality:    
        -  0,1     
      * -  Parameters:    
        -  :sidskey:`CellDimension`  

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

  #. The diffusion model defined here is only applicable to structured zones.
  #. For a structured zone, :sidskey:`IndexDimension = CellDimension`.

.. last line
