##
# rsInspectConstraints
# @author Juan Lara
# @date 2013-04-30
# @file rsInspectConstraints.py


import win32com.client
from win32com.client import constants

Application = win32com.client.Dispatch('XSI.Application').Application


##
# Load plugin event.
# @param in_reg: register
# @return Boolean
def XSILoadPlugin(in_reg):
    in_reg.Author = "jlara"
    in_reg.Name = "rsInspectConstraints"
    in_reg.Email = "info@rigstudio.com"
    in_reg.URL = "www.rigstudio.com"
    in_reg.Major = 1
    in_reg.Minor = 0

    in_reg.RegisterCommand("rsInspectConstraints", "rsInspectConstraints")
    in_reg.RegisterMenu(constants.siMenuMCPSelectSelBtnContextID, "rsInspectConstraints_Menu", False, False)
    return True


##
# Unload plugin event.
# @param in_reg: register
# @return Boolean
def XSIUnloadPlugin(in_reg):
    s_pluginName = in_reg.Name
    Application.LogMessage(str(s_pluginName) + str(" has been unloaded."), constants.siVerbose)
    return True


##
# Menu setup.
# @param in_ctxt: context
# @return Boolean
def rsInspectConstraints_Menu_Init(ctxt):
    oMenu = ctxt.Source
    oMenu.AddCommandItem("rsConstraints Properties", "rsInspectConstraints")
    return True


##
# Command setup.
# @param in_ctxt: context
# @return Boolean
def rsInspectConstraints_Init(in_ctxt):
    o_cmd = in_ctxt.Source
    o_cmd.Description = ""
    o_cmd.ReturnValue = True

    oArgs = o_cmd.Arguments
    oArgs.AddWithHandler("in_c_items", "Collection")
    return True


##
# Inspect the constraints properties from selected objects.
# @param in_c_items: XSICollection
# @return Boolean
def rsInspectConstraints_Execute(in_c_items):

    Application.InspectObj(in_c_items, constants.siConstraintKeyword, "", constants.siRecycle, "")
    return True
