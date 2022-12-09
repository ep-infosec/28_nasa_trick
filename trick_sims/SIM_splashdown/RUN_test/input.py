import math
exec(open("Modified_data/realtime.py").read())

# Initialize the position (CG) of the vehicle 3 meters about the
# surface of the water so that it drops into the water.
crewModule.dyn.position[0] = 0.0;
crewModule.dyn.position[1] = 0.0;
crewModule.dyn.position[2] = 3.0;

# Rotate the vehicle 120 degrees about the X axis.
xrot = math.radians(120.0);
crewModule.dyn.R[0][0] =  1.000000;
crewModule.dyn.R[0][1] =  0.000000;
crewModule.dyn.R[0][2] =  0.000000;
crewModule.dyn.R[1][0] =  0.000000;
crewModule.dyn.R[1][1] =  math.cos(xrot);
crewModule.dyn.R[1][2] = -math.sin(xrot);
crewModule.dyn.R[2][0] =  0.000000;
crewModule.dyn.R[2][1] =  math.sin(xrot);
crewModule.dyn.R[2][2] =  math.cos(xrot);

crewModule.dyn.mass_vehicle = 9300.0;
# If the vehicle mass is changed, the inertia tensor needs to be re-calculated.
crewModule.dyn.init_inertia_tensor(1,1,1);


# ==========================================
# Start the CM Display Graphics Client
#==========================================
varServerPort = trick.var_server_get_port();
CMDisplay_path = "models/CrewModuleGraphics/build/CrewModuleDisplay.jar"

if (os.path.isfile(CMDisplay_path)) :
    CMDisplay_cmd = "java -jar " \
                   + CMDisplay_path \
                   + " " + str(varServerPort) + " &" ;
    print(CMDisplay_cmd)
    os.system( CMDisplay_cmd);
else :
    print('==================================================================================')
    print('CrewModuleDisplay needs to be built. Please \"cd\" into ../models/CrewModuleGraphics and type \"mvn package\".')
    print('==================================================================================')
