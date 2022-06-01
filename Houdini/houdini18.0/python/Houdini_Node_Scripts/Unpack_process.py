#Created by MasatoTszuki at Mikros FX

node = hou.pwd()
geo = node.geometry()
resultgeo = hou.Geometry()

sops = hou.sopNodeTypeCategory()
#unpack
unpack_py = sops.nodeVerb('unpack')
unpack_py.setParms({'transfer_attributes': 'path'})
unpack_py.execute(geo,[geo])

#reconvert_ShapeName
for prim in geo.iterPrims():
    path = prim.attribValue("path")
    shape = path.split("/")[-1]

    prim.setAttribValue("path",shape)

#normal
normal_py = sops.nodeVerb('normal')
normal_py.execute(resultgeo,[geo])


node.geometry().clear()
node.geometry().merge(resultgeo)
