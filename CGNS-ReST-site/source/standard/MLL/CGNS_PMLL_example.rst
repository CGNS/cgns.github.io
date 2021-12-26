.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _PMLLexample:
   
CGNS/PMLL examples
------------------

The following examples create a 4x4x4 cube of hexahedral elements
using parallel data output. A cell-centered solution field and a
data array under a user-defined node are also created. Each process
writes a subset of the total data based on it's rank and the number
of processes.





Fortran Example
^^^^^^^^^^^^^^^


.. code-block:: fortran

          program fexample
    
    #ifdef WINNT
          include 'cgnswin_f.h'
    #endif
          include 'cgnslib_f.h'
          include 'mpif.h'
    
          integer nperside, totnodes, totelems
          parameter (nperside = 5)
          parameter (totnodes=nperside*nperside*nperside)
          parameter (totelems=(nperside-1)*(nperside-1)*(nperside-1))
    
          integer commsize, commrank, ierr
          integer i, j, k, n, nn, ne
          integer F, B, Z, E, S, Fs, Cx, Cy, Cz, A
          integer nnodes, nelems
          integer sizes(3), start, end
          real*4 fx(totnodes), fy(totnodes), fz(totnodes), fd(totelems)
          integer ie(8*totelems)
    
    !---- initialize MPI
          call MPI_INIT(ierr)
          call MPI_COMM_SIZE(MPI_COMM_WORLD, commsize, ierr)
          call MPI_COMM_RANK(MPI_COMM_WORLD, commrank, ierr)
    
    !---- open file and create base and zone
          sizes(1) = totnodes
          sizes(2) = totelems
          sizes(3) = 0
    
    !---- default is MPI_COMM_WORLD, but can set another
    !     communicator with this
    !     call cgp_mpi_comm_f(MPI_COMM_WORLD,ierr)
    
          call cgp_open_f('fexample.cgns', CG_MODE_WRITE, F, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cg_base_write_f(F, 'Base', 3, 3, B, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cg_zone_write_f(F, B, 'Zone', sizes, Unstructured, Z, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
    
    !---- print info
          if (commrank .eq. 0) then
            print *, 'writing',totnodes,' coordinates and', totelems,
         &           ' hex elements to fexample.cgns'
          endif
    
    !---- create data nodes for coordinates
          call cgp_coord_write_f(F, B, Z, RealSingle, 'CoordinateX',
         &                       Cx, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cgp_coord_write_f(F, B, Z, RealSingle, 'CoordinateY',
         &                       Cy, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cgp_coord_write_f(F, B, Z, RealSingle, 'CoordinateZ',
         &                       Cz, ierr)
    
    !---- number of nodes and range this process will write
          nnodes = (totnodes + commsize - 1) / commsize
          start  = nnodes * commrank + 1
          end    = nnodes * (commrank + 1)
          if (end .gt. totnodes) end = totnodes
    
    !---- create the coordinate data for this process
          nn = 1
          n  = 1
          do k=1,nperside
            do j=1,nperside
              do i=1,nperside
                if (n .ge. start .and. n .le. end) then
                  fx(nn) = i
                  fy(nn) = j
                  fz(nn) = k
                  nn = nn + 1
                endif
                n = n + 1
              enddo
            enddo
          enddo
    
    !---- write the coordinate data in parallel
          call cgp_coord_write_data_f(F, B, Z, Cx, start, end, fx, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cgp_coord_write_data_f(F, B, Z, Cy, start, end, fy, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cgp_coord_write_data_f(F, B, Z, Cz, start, end, fz, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
    
    !---- create data node for elements
          call cgp_section_write_f(F, B, Z, 'Hex', HEXA_8, 1, totelems,
         &                         0, E, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
    
    !---- number of elements and range this process will write
          nelems = (totelems + commsize - 1) / commsize
          start  = nelems * commrank + 1
          end    = nelems * (commrank + 1)
          if (end .gt. totelems) end = totelems
    
    !---- create the hex element data for this process
          nn = 0
          n  = 1
          do k=1,nperside-1
            do j=1,nperside-1
              do i=1,nperside-1
                if (n .ge. start .and. n .le. end) then
                  ne = i + nperside*((j-1)+nperside*(k-1))
                  ie(nn+1) = ne
                  ie(nn+2) = ne + 1
                  ie(nn+3) = ne + 1 + nperside
                  ie(nn+4) = ne + nperside
                  ne = ne + nperside*nperside
                  ie(nn+5) = ne
                  ie(nn+6) = ne + 1
                  ie(nn+7) = ne + 1 + nperside
                  ie(nn+8) = ne + nperside
                  nn = nn + 8
                endif
                n = n + 1
              enddo
            enddo
          enddo
    
    !---- write the element connectivity in parallel
          call cgp_elements_write_data_f(F, B, Z, E, start, end, ie, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
    
    !---- create a centered solution
          call cg_sol_write_f(F, B, Z, 'Solution', CellCenter, S, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cgp_field_write_f(F, B, Z, S, RealSingle, 'CellIndex',
         &                       Fs, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
    
    !---- create the field data for this process
          nn = 1
          do n=1, totelems
            if (n .ge. start .and. n .le. end) then
              fd(nn) = n
              nn = nn + 1
            endif
          enddo
    
    !---- write the solution field data in parallel
          call cgp_field_write_data_f(F, B, Z, S, Fs, start, end, fd, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
    
    !---- create user data under the zone and duplicate solution data
          call cg_goto_f(F, B, ierr, 'Zone_t', 1, 'end')
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cg_user_data_write_f('User Data', ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cg_gorel_f(F, ierr, 'User Data', 0, 'end')
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call cgp_array_write_f('CellIndex', RealSingle, 1, totelems,
         &                       A, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
    
    !---- write the array data in parallel
          call cgp_array_write_data_f(A, start, end, fd, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
    
    !---- close the file and terminate MPI
          call cgp_close_f(F, ierr)
          if (ierr .ne. CG_OK) call cgp_error_exit_f
          call MPI_FINALIZE(ierr)
          end
    


C example
^^^^^^^^^

.. code-block:: C

    #include <stdio.h>;
    #include <stdlib.h>;
    
    #include "pcgnslib.h"
    #include "mpi.h"
    
    #define NODES_PER_SIDE 5
    
    int main(int argc, char *argv[])
    {
        int comm_size, comm_rank;
        int tot_nnodes, tot_nelems, nnodes, nelems;
        int F, B, Z, E, S, Fs, A, Cx, Cy, Cz;
        int i, j, k, n, nn, ne;
        float *x, *y, *z, *d;
        cgsize_t sizes[3], *e, start, end, ncells;
        static char *outfile = "cexample.cgns";
    
        /* initialize MPI */
        MPI_Init(&argc,&argv);
        MPI_Comm_size(MPI_COMM_WORLD, &comm_size);
        MPI_Comm_rank(MPI_COMM_WORLD, &comm_rank);
    
        /* total number of nodes and hex elements */
        tot_nnodes = NODES_PER_SIDE * NODES_PER_SIDE * NODES_PER_SIDE;
        tot_nelems = (NODES_PER_SIDE-1) * (NODES_PER_SIDE-1) * (NODES_PER_SIDE-1);
     
        /* open the file and create base and zone */
        sizes[0] = tot_nnodes;
        sizes[1] = tot_nelems;
        sizes[2] = 0;
    
        /* the default here is to use MPI_COMM_WORLD,
           but this allows assigning of another communicator
        cgp_mpi_comm(MPI_COMM_WORLD); */
    
        if (cgp_open(outfile, CG_MODE_WRITE, &F) ||
            cg_base_write(F, "Base", 3, 3, &B) ||
            cg_zone_write(F, B, "Zone", sizes, Unstructured, &Z))
            cgp_error_exit();
    
        /* print info */
        if (comm_rank == 0) {
            printf("writing %d coordinates and %d hex elements to %s\n",
                tot_nnodes, tot_nelems, outfile);
        }
    
        /* create data nodes for coordinates */
        if (cgp_coord_write(F, B, Z, RealSingle, "CoordinateX", &Cx) ||
            cgp_coord_write(F, B, Z, RealSingle, "CoordinateY", &Cy) ||
            cgp_coord_write(F, B, Z, RealSingle, "CoordinateZ", &Cz))
            cgp_error_exit();
     
        /* number of nodes and range this process will write */
        nnodes = (tot_nnodes + comm_size - 1) / comm_size;
        start  = nnodes * comm_rank + 1;
        end    = nnodes * (comm_rank + 1);
        if (end &gt; tot_nnodes) end = tot_nnodes;
        
        /* create the coordinate data for this process */
        x = (float *)malloc(nnodes * sizeof(float));
        y = (float *)malloc(nnodes * sizeof(float));
        z = (float *)malloc(nnodes * sizeof(float));
        nn = 0;
        for (n = 1, k = 0; k &lt; NODES_PER_SIDE; k++) {
            for (j = 0; j &lt; NODES_PER_SIDE; j++) {
                for (i = 0; i &lt; NODES_PER_SIDE; i++, n++) {
                    if (n &gt;= start && n &lt;= end) {
                        x[nn] = (float)i;
                        y[nn] = (float)j;
                        z[nn] = (float)k;
                        nn++;
                    }
                }
            }
        }
    
        /* write the coordinate data in parallel */
        if (cgp_coord_write_data(F, B, Z, Cx, &start, &end, x) ||
            cgp_coord_write_data(F, B, Z, Cy, &start, &end, y) ||
            cgp_coord_write_data(F, B, Z, Cz, &start, &end, z))
            cgp_error_exit();
        
        /* create data node for elements */
        if (cgp_section_write(F, B, Z, "Hex", HEXA_8, 1, tot_nelems, 0, &E))
            cgp_error_exit();
     
        /* number of elements and range this process will write */
        nelems = (tot_nelems + comm_size - 1) / comm_size;
        start  = nelems * comm_rank + 1;
        end    = nelems * (comm_rank + 1);
        if (end &gt; tot_nelems) end = tot_nelems;
        
        /* create the hex element data for this process */
        e = (cgsize_t *)malloc(8 * nelems * sizeof(cgsize_t));
        nn = 0;
        for (n = 1, k = 1; k &lt; NODES_PER_SIDE; k++) {
            for (j = 1; j &lt; NODES_PER_SIDE; j++) {
                for (i = 1; i &lt; NODES_PER_SIDE; i++, n++) {
                    if (n &gt;= start && n &lt;= end) {
                        ne = i + NODES_PER_SIDE*((j-1)+NODES_PER_SIDE*(k-1));
                        e[nn++] = ne;
                        e[nn++] = ne + 1;
                        e[nn++] = ne + 1 + NODES_PER_SIDE;
                        e[nn++] = ne + NODES_PER_SIDE;
                        ne += NODES_PER_SIDE * NODES_PER_SIDE;
                        e[nn++] = ne;
                        e[nn++] = ne + 1;
                        e[nn++] = ne + 1 + NODES_PER_SIDE;
                        e[nn++] = ne + NODES_PER_SIDE;
                    }
                }
            }
        }
    
        /* write the element connectivity in parallel */
        if (cgp_elements_write_data(F, B, Z, E, start, end, e))
            cgp_error_exit();
    
        /* create a centered solution */
        if (cg_sol_write(F, B, Z, "Solution", CellCenter, &S) ||
            cgp_field_write(F, B, Z, S, RealSingle, "CellIndex", &Fs))
            cgp_error_exit();
    
        /* create the field data for this process */
        d = (float *)malloc(nelems * sizeof(float));
        nn = 0;
        for (n = 1; n &lt;= tot_nelems; n++) {
            if (n &gt;= start && n &lt;= end) {
                d[nn] = (float)n;
                nn++;
            }
        }
    
        /* write the solution field data in parallel */
        if (cgp_field_write_data(F, B, Z, S, Fs, &start, &end, d))
            cgp_error_exit();
    
        /* create user data under the zone and duplicate solution data */
        ncells = tot_nelems;
        if (cg_goto(F, B, "Zone_t", 1, NULL) ||
            cg_user_data_write("User Data") ||
            cg_gorel(F, "User Data", 0, NULL) ||
            cgp_array_write("CellIndex", RealSingle, 1, &ncells, &A))
            cgp_error_exit();
    
        /* write the array data in parallel */
        if (cgp_array_write_data(A, &start, &end, d))
            cgp_error_exit();
    
        /* close the file and terminate MPI */
        cgp_close(F);    
        MPI_Finalize();
        return 0;
    }


.. last_line
