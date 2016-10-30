#python

import lx, lxu, modo, traceback

NAME_CMD = "kelvin.quickScale"

class CMD_kelvin(lxu.command.BasicCommand):

    _last_used = 1.0

    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.dyna_Add("width", lx.symbol.sTYPE_DISTANCE)
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)

    def cmd_Flags(self):
        return lx.symbol.fCMD_POSTCMD | lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    @classmethod
    def set_last_used(cls, value):
        cls._last_used = value

    def cmd_DialogInit(self):
        self.attr_SetFlt(0, self._last_used)

    def basic_Execute(self, msg, flags):
        try:
            targetSize = self.dyna_Float(0) if self.dyna_IsSet(0) else 1.0
            self.set_last_used(targetSize)
            lx.eval("item.refSystem")
            lx.eval("select.typeFrom polygon;edge;vertex;item;pivot;center;ptag true")
            lx.eval("tool.set actr.origin on")

            lx.eval("@absolute.pl grab")
            lx.eval("user.value lux_absolute_size_Uniform %s" % targetSize)
            lx.eval("@absolute.pl scale")

            lx.eval("item.refSystem {}")
            lx.eval("tool.clearTask axis")
            lx.eval("select.typeFrom item;pivot;center;edge;polygon;vertex;ptag true")

        except:
            traceback.print_exc()


lx.bless(CMD_kelvin, NAME_CMD)
