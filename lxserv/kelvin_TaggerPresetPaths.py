# python

try:
    import tagger
    tagger.TaggerPresetPaths().add_path("kit_mecco_kelvin:Kelvin/kelvin_materials")

except:
    # Tagger is either not installed, or an older version.
    pass
