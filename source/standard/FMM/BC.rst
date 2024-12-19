.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _BCFigure:

BC Figure
=========


.. container:: fighead2
  
   **BC Node**
   
   (See :ref:`ZoneBC_t <ZoneBCFigure>`  figure)
     

.. container:: columns


  .. container:: left

    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`PointList`                    
          * -  Label:           
            -  :sidsref:`IndexArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`cgsize_t`                    
          * -  Dimensions:           
            -  2                   
          * -  Dimension Values:            
            -  :sidskey:`IndexDimension` , :sidskey:`ListLength[]`                    
          * -  Data:           
            -  List of indices representing vertices or boundary elements                   
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`ListLength`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidsref:`InwardNormalIndex`                    
          * -  Label:           
            -  ":sidskey:`int[IndexDimension]` "                   
          * -  Data-Type:           
            -  :sidskey:`I4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  :sidskey:`IndexDimension`                    
          * -  Data:           
            -  Index of inward normal                   
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`IndexDimension`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidsref:`InwardNormalList`                    
          * -  Label:           
            -  :sidsref:`IndexArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`R4`  or :sidskey:`R8`                    
          * -  Dimensions:           
            -  2                   
          * -  Dimension Values:            
            -  :sidskey:`PhysicalDimension` , :sidskey:`ListLength[]`                    
          * -  Data:           
            -  Vectors normal to patch pointing in                   
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`PhysicalDimension` , :sidskey:`ListLength`         
    
    .. container:: figelem2
            
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
    
    .. container:: figelem2
            
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
    
    .. container:: figelem2
            
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
    
    .. container:: figelem2
            
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
    
    .. container:: figelem2
            
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

  .. container:: right

    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`PointRange`                    
          * -  Label:            
            -  :sidsref:`IndexRange_t`                    
          * -  Data-Type:           
            -  :sidskey:`cgsize_t`                    
          * -  Dimensions:           
            -  2                   
          * -  Dimension Values:            
            -  :sidskey:`IndexDimension` ,2                   
          * -  Data:           
            -  :sidskey:`Begin[]` , :sidskey:`End[]`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`IndexDimension`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`GridLocation`                    
          * -  Label:            
            -  :sidsref:`GridLocation_t`                    
          * -  See:           
            -  :ref:`FlowSolution_t                figure <FlowSolutionFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`BCProperty`                    
          * -  Label:           
            -  :sidsref:`BCProperty_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:            
            -  :ref:`BCProperty_t figure <BCPropertyFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`FamilyName`                    
          * -  Label:           
            -  :sidsref:`FamilyName_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  Name of CFD family                   
          * -  Cardinality:           
            -  0,1        
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`User defined`                    
          * -  Label:           
            -  :sidskey:`AdditionalFamilyName_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  Name of CFD family                   
          * -  Cardinality:           
            -  0,N        
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`BCDataSet_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`BCTypeSimple`  value                   
          * -  Cardinality:           
            -  0, *N*                    
          * -  Parameters:           
            -  :sidskey:`ListLength`                    
          * -  Functions:           
            -  :sidsref:`ListLength`                    
          * -  Child Nodes:           
            -  :ref:`BCDataSet_t figure <BCDataSetFigure>`         
    
    .. container:: figelem2
            
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

            
.. note::

  #. The nodes :sidskey:`PointRange` and :sidskey:`PointList`, provide different ways of defining the patch. Only one of them may be used.
  #. :sidskey:`InwardNormalIndex` is only meaningful for structured zones.
  #. :sidskey:`cgsize_t` is determined by the application from which the node is written. For a 32-bit application, :sidskey:`cgsize_t` will be :sidskey:`I4`, and :sidskey:`I8` for a 64-bit application.


.. last line
