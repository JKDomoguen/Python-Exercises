    # rotated_images_arr1 = rotated_images_arr[:len(rotated_images_arr)//4]
    # rotated_images_arr2 = rotated_images_arr[len(rotated_images_arr)//4:2*len(rotated_images_arr)//4]
    # rotated_images_arr3 = rotated_images_arr[2*len(rotated_images_arr)//4:3*len(rotated_images_arr)//4]
    # rotated_images_arr4 = rotated_images_arr[3*len(rotated_images_arr)//4:]

        # npz_path1 = save_to_npz(rotated_images_arr1,dst_path,'first')
        # npz_path2 = save_to_npz(rotated_images_arr2,dst_path,'second')
        # npz_path3 = save_to_npz(rotated_images_arr3,dst_path,'third')
        # npz_path4 = save_to_npz(rotated_images_arr4,dst_path,'fourth')

        from PIL import Image
        img_obj = Image.fromarray((img_array).astype('uint8'))
        name = npz_path[9:24]
        img_obj.save('./'+npz_path[9:24]+'.jpg')


if __name__ == '__main__':
    # path = join(os.getcwd(),'saved_folder\\first.npz')
    # load_extract_data(path)
    main(CONFIG)
#     img_path = './lena.png'
#     from PIL import Image
#     im = Image.open(img_path)
#     # im.show()
#     rot_img_array = rotate_image(img_path)
#     # print(rot_img_array.shape)
#     img_obj = Image.fromarray((rot_img_array).astype('uint8'))
#     img_obj.save('./rotated_lena.jpg')
