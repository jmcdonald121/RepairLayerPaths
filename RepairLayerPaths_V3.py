import arcpy
from arcpy import env
env.workspace = r"C:/Users/mcdonald/Documents/Projects/BG_Application_Prototype/DRGs/DRG_Layers_Test"
NewMappedPath = r"X:/Image_Base_Data/DRGs/State Plane South Quads NoCollarsTIFs/24K_TIFs" #Note: Can use forward slashes for the Mapped Drive Path
NewUNC = r"\\nrgishome\GIS_DATA\ImageBase\DRGs\State Plane South Quads NoCollarsTIFs\24K_TIFs" #Note: Can not use forward slashes for the UNC path, unlike the Mapped Drive Path. 

LyrList = arcpy.ListFiles("*.lyr")
print LyrList
for Lyr in LyrList:
    try:
        print ""
        LyrPath = "C:/Users/mcdonald/Documents/Projects/BG_Application_Prototype/DRGs/DRG_Layers_Test/" + Lyr
        print LyrPath
        Lyrfix = arcpy.mapping.Layer(LyrPath)
        print Lyrfix.name
        print Lyrfix.workspacePath
        if Lyrfix.workspacePath == r"X:\DATA\DRGs" + u"\u005C": #Note: The workspace path is stored with a trailing backslash (\), hence the unicode value in the IF statement, while the findAndReplaceWorkspacePath does not use a trailing backslash.
            Lyrfix.findAndReplaceWorkspacePath(r"X:\DATA\DRGs", NewMappedPath) #Note: Note the difference between workspacePath and the findAndReplaceWorkspacePath. One requires a trailing slash, while the other does not.
            Lyrfix.save()
            print "Saved Layer File"
            print ""
    except arcpy.ExecuteError:
        print arcpy.GetMessages(2)
    except:
        print "There has been an error with this statement"
            
