.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardCGIOExamples:
   
Code Examples
=============

The following examples build the database file shown in the :ref:`example database figure <ExampleNodeDatabase>`.

C example
---------

.. code-block:: c

  /*
   Sample CGIO test program to build files illustrated
   in example database figure.
   */
   
   #include <stdio.h>
   #include <ctype.h>
   #include <string.h>
   
   #include "cgns_io.h"
   
   void print_child_list(int cgio_num,double node_id);
   
   int main ()
   {
     /* --- Node header character strings */
      char label[CGIO_MAX_LABEL_LENGTH+1];
      char data_type[CGIO_MAX_DATATYPE_LENGTH+1];
   
     /* --- Database identifier */
     int cgio_num, cgio_num2;
   
     /* --- Node id variables */
      double root_id,parent_id,child_id,tmp_id,root_id_file2;
   
     /* --- Data to be stored in database */
      float a[3][4] = {{1.1,2.1,3.1,4.1},
                       {1.2,2.2,3.2,4.2},
                       {1.3,2.3,3.3,4.3}
                      };
      cgsize_t a_dimensions[2] = {4,3};
   
      int c[6] = {1,2,3,4,5,6};
      cgsize_t c_dimension = 6;
   
     /* --- miscellaneous variables */
      int i, j;
      int error_state = 1;
      int num_dims, d[6];
      cgsize_t dim_d, dims_b[2];
      float b[3][4];
   
     /* ------ begin source code ----- */
   
     /* --- set database error flag to abort on error */
      cgio_error_abort(error_state);
   
     /* -------- build file: file_two.cgio ---------- */
     /* --- 1.) open database
            2.) create three nodes at first level
            3.) put label on node f3
            4.) put some data in node f3
            5.) create two nodes below f3
            6.) close database */
   
      cgio_open_file("file_two.cgio",CGIO_MODE_WRITE,CGIO_FILE_NONE,&cgio_num);
      cgio_get_root_id(cgio_num,&root_id);
      root_id_file2 = root_id;
      cgio_create_node(cgio_num,root_id,"f1",&tmp_id);
      cgio_create_node(cgio_num,root_id,"f2",&tmp_id);
      cgio_create_node(cgio_num,root_id,"f3",&parent_id);
      cgio_set_label(cgio_num,parent_id,"label on node f3");
   
      cgio_set_dimensions(cgio_num,parent_id,"R4",2,a_dimensions);
      cgio_write_all_data(cgio_num,parent_id,a);
   
      cgio_create_node(cgio_num,parent_id,"f4",&child_id);
      cgio_create_node(cgio_num,parent_id,"f5",&child_id);
      cgio_close_file(cgio_num);
   
     /* -------- build file: file_one.cgio ---------- */
     /* open database and create three nodes at first level */
      cgio_open_file("file_one.cgio",CGIO_MODE_WRITE,CGIO_FILE_NONE,&cgio_num);
      cgio_get_root_id(cgio_num,&root_id);
      cgio_create_node(cgio_num,root_id,"n1",&tmp_id);
      cgio_create_node(cgio_num,root_id,"n2",&tmp_id);
      cgio_create_node(cgio_num,root_id,"n3",&tmp_id);
   
     /* put three nodes under n1 (two regular and one link) */
      cgio_get_node_id(cgio_num,root_id,"n1",&parent_id);
      cgio_create_node(cgio_num,parent_id,"n4",&tmp_id);
      cgio_create_link(cgio_num,parent_id,"l3","file_two.cgio","/f3",&tmp_id);
      cgio_create_node(cgio_num,parent_id,"n5",&tmp_id);
   
     /* put two nodes under n4 */
      cgio_get_node_id(cgio_num,parent_id,"n4",&child_id);
      cgio_create_node(cgio_num,child_id,"n6",&tmp_id);
      cgio_create_node(cgio_num,child_id,"n7",&tmp_id);
   
     /* put one nodes under n6 */
      cgio_get_node_id(cgio_num,root_id,"/n1/n4/n6",&parent_id);
      cgio_create_node(cgio_num,parent_id,"n8",&tmp_id);
   
     /* put three nodes under n3 */
      cgio_get_node_id(cgio_num,root_id,"n3",&parent_id);
      cgio_create_node(cgio_num,parent_id,"n9",&tmp_id);
      cgio_create_node(cgio_num,parent_id,"n10",&tmp_id);
      cgio_create_node(cgio_num,parent_id,"n11",&tmp_id);
   
     /* put two nodes under n9 */
      cgio_get_node_id(cgio_num,parent_id,"n9",&child_id);
      cgio_create_node(cgio_num,child_id,"n12",&tmp_id);
      cgio_create_node(cgio_num,child_id,"n13",&tmp_id);
   
     /* put label and data in n13 */
      cgio_set_label(cgio_num,tmp_id,"Label on Node n13");
      cgio_set_dimensions(cgio_num,tmp_id,"I4",1,&c_dimension);
      cgio_write_all_data(cgio_num,tmp_id,c);
   
     /* put two nodes under n10 (one normal, one link) */
      cgio_get_node_id(cgio_num,root_id,"/n3/n10",&parent_id);
      cgio_create_link(cgio_num,parent_id,"l1"," ","/n3/n9/n13",&tmp_id);
      cgio_create_node(cgio_num,parent_id,"n14",&tmp_id);
   
     /* put two nodes under n11 (one normal, one link) */
      cgio_get_node_id(cgio_num,root_id,"/n3/n11",&parent_id);
      cgio_create_link(cgio_num,parent_id,"l2"," ","/n3/n9/n13",&tmp_id);
      cgio_create_node(cgio_num,parent_id,"n15",&tmp_id);
   
     /* ----------------- finished building file_one.cgio ------------- */
   
     /* ------------- access and print data --------------- */
   
     /* access data in node f3 (file_two.cgio) through link l3 */
      cgio_get_node_id(cgio_num,root_id,"/n1/l3",&tmp_id);
      cgio_get_label(cgio_num,tmp_id,label);
      cgio_get_data_type(cgio_num,tmp_id,data_type);
      cgio_get_dimensions(cgio_num,tmp_id,&num_dims,dims_b);
      cgio_read_all_data_type(cgio_num,tmp_id,"R4",b);
      printf (" node f3 through link l3:\n");
      printf ("   label       = %s\n",label);
      printf ("   data_type   = %s\n",data_type);
      printf ("   num of dims = %5d\n",num_dims);
      printf ("   dim vals    = %5d %5d\n",dims_b[0],dims_b[1]);
      printf ("   data:\n");
      for (i=0; i<=3; i++)
        {
          for (j=0; j<=2; j++)
            {
              printf("     %10.2f",b[j][i]);
            };
          printf("\n");
        }
   
     /* access data in node n13 */
      cgio_get_node_id(cgio_num,root_id,"/n3/n9/n13",&tmp_id);
      cgio_get_label(cgio_num,tmp_id,label);
      cgio_get_data_type(cgio_num,tmp_id,data_type);
      cgio_get_dimensions(cgio_num,tmp_id,&num_dims,&dim_d);
      cgio_read_all_data_type(cgio_num,tmp_id,"I4",d);
      printf (" node n13:\n");
      printf ("   label       = %s\n",label);
      printf ("   data_type   = %s\n",data_type);
      printf ("   num of dims = %5d\n",num_dims);
      printf ("   dim val     = %5d\n",dim_d);
      printf ("   data:\n");
      for (i=0; i<=5; i++)
        {
          printf("     %-4d",d[i]);
        }
      printf("\n\n");
   
     /* access data in node n13 through l1 */
      cgio_get_node_id(cgio_num,root_id,"/n3/n10/l1",&tmp_id);
      cgio_get_label(cgio_num,tmp_id,label);
      cgio_read_all_data_type(cgio_num,tmp_id,"I4",d);
      printf (" node n13 through l1:\n");
      printf ("   label       = %s\n",label);
      printf ("   data:\n");
      for (i=0; i<=5; i++)
        {
          printf("     %-4d",d[i]);
        }
      printf("\n\n");
   
     /* access data in node n13 through l2 */
      cgio_get_node_id(cgio_num,root_id,"/n3/n11/l2",&tmp_id);
      cgio_get_label(cgio_num,tmp_id,label);
      cgio_read_all_data_type(cgio_num,tmp_id,"I4",d);
      printf (" node n13 through l2:\n");
      printf ("   label       = %s\n",label);
      printf ("   data:\n");
      for (i=0; i<=5; i++)
        {
          printf("     %-4d",d[i]);
        }
      printf("\n\n");
   
     /* print list of children under root node */
      print_child_list(cgio_num,root_id);
   
     /* print list of children under n3 */
      cgio_get_node_id(cgio_num,root_id,"/n3",&tmp_id);
      print_child_list(cgio_num,tmp_id);
   
     /* re-open file_two and get new root id */
      cgio_open_file("file_two.cgio",CGIO_MODE_READ,CGIO_FILE_NONE,&cgio_num2);
      cgio_get_root_id(cgio_num2,&root_id);
      printf (" Comparison of root id:\n");
      printf ("   file_two.cgio original root id = %g\n",root_id_file2);
      printf ("   file_two.cgio new      root id = %g\n",root_id);
   
      cgio_close_file(cgio_num);
      cgio_close_file(cgio_num2);
      return 0;
   }
   
   void print_child_list(int cgio_num, double node_id)
   {
   
   /*
      print table of children given a parent node-id
   */
      char node_name[CGIO_MAX_NAME_LENGTH+1];
      int i, num_children, num_ret;
   
      cgio_get_name(cgio_num,node_id,node_name);
      cgio_number_children(cgio_num,node_id,&num_children);
      printf ("Parent Node Name = %s\n",node_name);
      printf ("  Number of Children = %2d\n",num_children);
      printf ("  Children Names:\n");
      for (i=1; i<=num_children; i++)
        {
          cgio_children_names(cgio_num,node_id,i,1,CGIO_MAX_NAME_LENGTH+1,
              &num_ret,node_name);
          printf ("     %s\n",node_name);
        }
       printf ("\n");
   }
   
The resulting output is:

.. parsed-literal::

  node f3 through link l3:
     label       = label on node f3
     data_type   = R4
     num of dims =     2
     dim vals    =     4     3
     data:
             1.10           1.20           1.30
             2.10           2.20           2.30
             3.10           3.20           3.30
             4.10           4.20           4.30
  node n13:
     label       = Label on Node n13
     data_type   = I4
     num of dims =     1
     dim val     =     6
     data:
       1        2        3        4        5        6
  
  node n13 through l1:
     label       = Label on Node n13
     data:
       1        2        3        4        5        6
  
  node n13 through l2:
     label       = Label on Node n13
     data:
       1        2        3        4        5        6
  
  Parent Node Name = ADF MotherNode
    Number of Children =  3
    Children Names:
       n1
       n2
       n3
  
  Parent Node Name = n3
    Number of Children =  3
    Children Names:
       n9
       n10
       n11
  
  Comparison of root id:
     file_two.cgio original root id = 2
     file_two.cgio new      root id = 3
  

Fortran example
---------------

.. code-block:: fortran

        PROGRAM TEST
  C
  C     SAMPLE ADF TEST PROGRAM TO BUILD FILES ILLUSTRATED
  C     IN THE EXAMPLE DATABASE FIGURE
  C
        INCLUDE 'cgns_io_f.h'
  C
        PARAMETER (MAXCHR=32)
  C
        CHARACTER*(MAXCHR) TSTLBL,DTYPE
        CHARACTER*(MAXCHR) FNAM,PATH
  C
        REAL*8 RID,PID,CID,TMPID,RIDF2
        REAL A(4,3),B(4,3)
        INTEGER*4 IC(6),ID(6)
        INTEGER IERR,ICGIO,ICGIO2
        INTEGER IDIM(2),IDIMA(2),IDIMC,IDIMD
  C
        DATA A /1.1,2.1,3.1,4.1,
       X        1.2,2.2,3.2,4.2,
       X        1.3,2.3,3.3,4.3/
        DATA IDIMA /4,3/
  C
        DATA IC /1,2,3,4,5,6/
        DATA IDIMC /6/
  C
  C     SET ERROR FLAG TO ABORT ON ERROR
  C
        CALL CGIO_ERROR_ABORT_F(1)
  C
  C *** 1.) OPEN 1ST DATABASE (ADF_FILE_TWO.ADF)
  C     2.) CREATE THREE NODES AT FIRST LEVEL
  C     3.) PUT LABEL ON NODE F3
  C     4.) PUT DATA IN F3
  C     5.) CREATE TWO NODES BELOW F3
  C     6.) CLOSE DATABASE
  C
        CALL CGIO_OPEN_FILE_F('file_two.cgio',CGIO_MODE_WRITE,
       &                      CGIO_FILE_ADF,ICGIO,IERR)
        CALL CGIO_GET_ROOT_ID_F(ICGIO,RID,IERR)
        RIDF2 = RID
        CALL CGIO_CREATE_NODE_F(ICGIO,RID,'F1',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,RID,'F2',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,RID,'F3',PID,IERR)
        CALL CGIO_SET_LABEL_F(ICGIO,PID,'LABEL ON NODE F3',IERR)
        CALL CGIO_SET_DIMENSIONS_F(ICGIO,PID,'R4',2,IDIMA,IERR)
        CALL CGIO_WRITE_ALL_DATA_F(ICGIO,PID,A,IERR)
  C
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'F4',CID,IERR)
  C
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'F5',CID,IERR)
  C
        CALL CGIO_CLOSE_FILE_F(ICGIO,IERR)
  C
  C *** 1.) OPEN 2ND DATABASE
  C     2.) CREATE NODES
  C     3.) PUT DATA IN N13
  C
        CALL CGIO_OPEN_FILE_F('file_one.cgio',CGIO_MODE_WRITE,
       &                      CGIO_FILE_ADF,ICGIO,IERR)
        CALL CGIO_GET_ROOT_ID_F(ICGIO,RID,IERR)
  C
  C     THREE NODES UNDER ROOT
  C
        CALL CGIO_CREATE_NODE_F(ICGIO,RID,'N1',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,RID,'N2',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,RID,'N3',TMPID,IERR)
  C
  C     THREE NODES UNDER N1 (TWO REGULAR AND ONE LINK)
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'N1',PID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'N4',TMPID,IERR)
        CALL CGIO_CREATE_LINK_F(ICGIO,PID,'L3','file_two.cgio','/F3',
       &                        TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'N5',TMPID,IERR)
  C
  C     TWO NODES UNDER N4
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,PID,'N4',CID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,CID,'N6',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,CID,'N7',TMPID,IERR)
  C
  C     ONE NODE UNDER N6
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'/N1/N4/N6',PID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'N8',TMPID,IERR)
  C
  C     THREE NODES UNDER N3
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'N3',PID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'N9',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'N10',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'N11',TMPID,IERR)
  C
  C     TWO NODES UNDER N9
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,PID,'N9',CID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,CID,'N12',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,CID,'N13',TMPID,IERR)
  C
  C     PUT LABEL AND DATA IN N13
  C
        CALL CGIO_SET_LABEL_F(ICGIO,TMPID,'LABEL ON NODE N13',IERR)
        CALL CGIO_SET_DIMENSIONS_F(ICGIO,TMPID,'I4',1,IDIMC,IERR)
        CALL CGIO_WRITE_ALL_DATA_F(ICGIO,TMPID,IC,IERR)
  C
  C     TWO NODES UNDER N10
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'/N3/N10',PID,IERR)
        CALL CGIO_CREATE_LINK_F(ICGIO,PID,'L1','','/N3/N9/N13',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'N14',TMPID,IERR)
  C
  C     TWO NODES UNDER N11
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'/N3/N11',PID,IERR)
        CALL CGIO_CREATE_LINK_F(ICGIO,PID,'L2','','/N3/N9/N13',TMPID,IERR)
        CALL CGIO_CREATE_NODE_F(ICGIO,PID,'N15',TMPID,IERR)
  C
  C *** READ AND PRINT DATA FROM NODES
  C     1.) NODE F5 THROUGH LINK L3
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'/N1/L3',PID,IERR)
        CALL CGIO_GET_LABEL_F(ICGIO,PID,TSTLBL,IERR)
        CALL CGIO_GET_DATA_TYPE_F(ICGIO,PID,DTYPE,IERR)
        CALL CGIO_GET_DIMENSIONS_F(ICGIO,PID,NUMDIM,IDIM,IERR)
        CALL CGIO_READ_ALL_DATA_TYPE_F(ICGIO,PID,'R4',B,IERR)
        PRINT *,' NODE F3 THROUGH LINK L3:'
        PRINT *,'   LABEL       = ',TSTLBL
        PRINT *,'   DATA TYPE   = ',DTYPE
        PRINT *,'   NUM OF DIMS = ',NUMDIM
        PRINT *,'   DIM VALS    = ',IDIM
        PRINT *,'   DATA:'
        WRITE(*,100)((B(J,I),I=1,3),J=1,4)
    100 FORMAT(5X,3F10.2)
  C
  C     2.) N13
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'N3/N9/N13',PID,IERR)
        CALL CGIO_GET_LABEL_F(ICGIO,PID,TSTLBL,IERR)
        CALL CGIO_GET_DATA_TYPE_F(ICGIO,PID,DTYPE,IERR)
        CALL CGIO_GET_DIMENSIONS_F(ICGIO,PID,NUMDIM,IDIMD,IERR)
        CALL CGIO_READ_ALL_DATA_TYPE_F(ICGIO,PID,'I4',ID,IERR)
        PRINT *,' '
        PRINT *,' NODE N13:'
        PRINT *,'   LABEL       = ',TSTLBL
        PRINT *,'   DATA TYPE   = ',DTYPE
        PRINT *,'   NUM OF DIMS = ',NUMDIM
        PRINT *,'   DIM VALS    = ',IDIMD
        PRINT *,'   DATA:'
        WRITE(*,200)(ID(I),I=1,6)
    200 FORMAT(5X,6I6)
  C
  C     3.) N13 THROUGH L1
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'N3/N10/L1',TMPID,IERR)
        CALL CGIO_GET_LABEL_F(ICGIO,TMPID,TSTLBL,IERR)
        CALL CGIO_READ_ALL_DATA_TYPE_F(ICGIO,TMPID,'I4',ID,IERR)
        PRINT *,' '
        PRINT *,' NODE N13 THROUGH LINK L1:'
        PRINT *,'   LABEL       = ',TSTLBL
        PRINT *,'   DATA:'
        WRITE(*,200)(ID(I),I=1,6)
  C
  C     4.) N13 THROUTH L2
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'N3/N11/L2',CID,IERR)
        CALL CGIO_GET_LABEL_F(ICGIO,CID,TSTLBL,IERR)
        CALL CGIO_READ_ALL_DATA_TYPE_F(ICGIO,CID,'I4',ID,IERR)
        PRINT *,' '
        PRINT *,' NODE N13 THROUGH LINK L2:'
        PRINT *,'   LABEL       = ',TSTLBL
        PRINT *,'   DATA:'
        WRITE(*,200)(ID(I),I=1,6)
  C
  C     PRINT LIST OF CHILDREN UNDER ROOT NODE
  C
        CALL PRTCLD(ICGIO,RID)
  C
  C     PRINT LIST OF CHILDREN UNDER N3
  C
        CALL CGIO_GET_NODE_ID_F(ICGIO,RID,'N3',PID,IERR)
        CALL PRTCLD(ICGIO,PID)
  C
  C     REOPEN ADF_FILE_TWO AND GET NEW ROOT ID
  C
        CALL CGIO_OPEN_FILE_F('file_two.cgio',CGIO_MODE_READ,
       &                      CGIO_FILE_ADF,ICGIO2,IERR)
        CALL CGIO_GET_ROOT_ID_F(ICGIO2,RID,IERR)
        PRINT *,' '
        PRINT *,' COMPARISON OF ROOT ID: '
        PRINT *,' file_two.cgio ORIGINAL ROOT ID = ',RIDF2
        PRINT *,' file_two.cgio NEW ROOT ID      = ',RID
  C
        CALL CGIO_CLOSE_FILE_F(ICGIO,IERR)
        CALL CGIO_CLOSE_FILE_F(ICGIO2,IERR)
  C
        STOP
        END
  C
  C ************* SUBROUTINES ****************
  C
        SUBROUTINE PRTCLD(ICGIO,PID)
  C
  C *** PRINT TABLE OF CHILDREN GIVEN A PARENT NODE-ID
  C
        PARAMETER (MAXCLD=10)
        PARAMETER (MAXCHR=32)
        REAL*8 PID
        CHARACTER*(MAXCHR) NODNAM,NDNMS(MAXCLD)
        CALL CGIO_GET_NAME_F(ICGIO,PID,NODNAM,IERR)
        CALL CGIO_NUMBER_CHILDREN_F(ICGIO,PID,NUMC,IERR)
        WRITE(*,120)NODNAM,NUMC
    120 FORMAT(/,' PARENT NODE NAME = ',A,/,
       X       '     NUMBER OF CHILDREN = ',I2,/,
       X       '     CHILDREN NAMES:')
        NLEFT = NUMC
        ISTART = 1
  C     --- TOP OF DO-WHILE LOOP
    130 CONTINUE
           CALL CGIO_CHILDREN_NAMES_F(ICGIO,PID,ISTART,MAXCLD,MAXCHR,
       X                              NUMRET,NDNMS,IERR)
           WRITE(*,140)(NDNMS(K),K=1,NUMRET)
    140    FORMAT(8X,A)
           NLEFT = NLEFT - MAXCLD
           ISTART = ISTART + MAXCLD
        IF (NLEFT .GT. 0) GO TO 130
        RETURN
        END
  
The resulting output is:

.. parsed-literal::

 NODE F3 THROUGH LINK L3:
    LABEL       = LABEL ON NODE F3
    DATA TYPE   = R4
    NUM OF DIMS =  2
    DIM VALS    =  4 3
    DATA:
           1.10      1.20      1.30
           2.10      2.20      2.30
           3.10      3.20      3.30
           4.10      4.20      4.30

  NODE N13:
    LABEL       = LABEL ON NODE N13
    DATA TYPE   = I4
    NUM OF DIMS =  1
    DIM VALS    =  6
    DATA:
          1     2     3     4     5     6

  NODE N13 THROUGH LINK L1:
    LABEL       = LABEL ON NODE N13
    DATA:
          1     2     3     4     5     6

  NODE N13 THROUGH LINK L2:
    LABEL       = LABEL ON NODE N13
    DATA:
          1     2     3     4     5     6

 PARENT NODE NAME = ADF MotherNode
     NUMBER OF CHILDREN =  3
     CHILDREN NAMES:
        N1
        N2
        N3

 PARENT NODE NAME = N3
     NUMBER OF CHILDREN =  3
     CHILDREN NAMES:
        N9
        N10
        N11

  COMPARISON OF ROOT ID:
  file_two.cgio ORIGINAL ROOT ID =   2.
  file_two.cgio NEW ROOT ID      =   3.


.. last line
