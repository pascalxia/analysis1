import nibabel as nib

img = nib.load('ds107_sub001_highres.nii')
data = img.get_data()
type(data)
