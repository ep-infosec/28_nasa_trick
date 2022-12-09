| [Home](/trick) → [Documentation Home](../Documentation-Home) → Running a Simulation |
|------------------------------------------------------------------|

S_main_${TRICK_HOST_CPU}.exe is generated by the CP and is the simulation main executable program.

The runtime configuration of the executive and its associated support utilities may be manipulated through entries in the simulation input file. The input file is described in detail in Input_File.

The command line for the runtime executive is:

```
S_main_${TRICK_HOST_CPU}.exe [trick_version] [sie]
       RUN_<name>/<input_file_name> [-d]
       [-O <output_file_path>]
       [-OO <output_file_path>]
       [-u <user_defined_arguments>]
```

- The first argument in the command line must be the simulation input file name. The input file name can be in the form of a full path name but MUST have a RUN_<name> directory immediately above the input file name. By default, all the simulation output is directed to this RUN_<name> directory. The standard <input_file_name> is input.py; however, a simulation could be started from a checkpoint file by substituting chkpnt_<time> in for <input_file_name> for non-Master/Slave and non-Import/Export simulations. For Master/Slave and Import/Export simulations you must have the simulation running, and the simulation must be in a freeze state before reloading a checkpoint.
- The trick_version option will tell what version of Trick built the S_main executable.
- The sie option will generate the smart input editor (SIE) resource file (CP will by default invoke the S_main executable with the sie option to generate this file).
- The '-d' argument is optional and, if specified, starts the simulation in an input file verification mode. In this mode the entire input file is read, echoed to standard out, and then the simulation exits without calling any jobs listed in the S_define file. This mode helps debug input file syntax errors.
- The '-O <output_file_path>' option allows the user to specify the directory to which simulation data log files will be written. If this option is omitted, the RUN_<name> directory is used.
- The '-OO <output_file_path>' option allows the user to specify the directory to which ALL simulation output files will be written. If this option is omitted, the RUN_<name> directory is used.
- The '-u' option specifies that all remaining arguments are meant to be used by user supplied jobs. All arguments after the -u can be accessed internal to the simulation jobs by calling the get_cmnd_args() function of the executive as illustrated below. In a master/slave simulation, the master's -u args will be passed to the slave.

The following code example shows how a function can access the command line arguments during execution.

```c++
#include "trick/command_line_protos.h"

void test_job( void ) {
    int num_args ;
    char **args ;
    int ii ;
    num_args = command_line_args_get_argc() ;
    args = command_line_args_get_argv() ;
    for( ii = 0 ; ii < num_args ; ii++ )
        printf( "argument #%d = %s\n" , ii , args[ii] ) ;
    return ;
}
```

[Continue to Input File](Input-File)