import isoBlockProgramFunctions as Func

#Ensure equipment is connected
if not Func.SetupComports():
    Func.UpdateTextArea('Unable to set up test equipment.  '
                        'Check the test equipment connections '
                        'and be sure they are powered on.  You '
                        'must restart the test program to attempt '
                        'equipment setup again.')

Func.LoadGUI()
