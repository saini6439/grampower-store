  document.addEventListener('DOMContentLoaded', function() {

        var files_photo = []
        FilePond.registerPlugin(FilePondPluginFileValidateSize);
        FilePond.registerPlugin(FilePondPluginFileValidateType);
        FilePond.setOptions({
            allowMultiple:true
        })
        const inputElement = document.querySelector('input[type="file"]');
        const pond = FilePond.create( inputElement, {
            acceptedFileTypes:['image/png', 'image/jpeg'],
            onaddfile: (err, fileItem) => {
                if (!err) {
                files_photo.push(fileItem.file)
                }
                console.log(files_photo)
            },
            onremovefile: (err, fileItem) => {
                const index = files_photo.indexOf(fileItem.file)
                if (index > -1) {
                    files_photo.splice(index, 1)
                }
                console.log(_photo)
            }
        } );

        var selectedFile = [];
        const fileInput = document.getElementById('cover');
        fileInput.onchange = () => {
          selectedFile.push(fileInput.files[0]);
        }


                var formData = new FormData();
         $(document).on('click', '#saveBtn', function(e) {
                 var products = fetchCategoryArray();
            formData.append('length',files_photo.length)
            formData.append('cover', selectedFile[0])
            formData.append('name', $('#name').val())
            formData.append('about', $('#about').val())
            formData.append('products', products)
            formData.append('lat', $('#lat').val())
            formData.append('long', $('#long').val())
            formData.append('sundayfrom_hour', $('#sundayfrom_hour').val())
            formData.append('sundayto_hour', $('#sundayto_hour').val())
            formData.append('mondayfrom_hour', $('#mondayfrom_hour').val())
            formData.append('mondayto_hour', $('#mondayto_hour').val())
            formData.append('tuesdayfrom_hour', $('#tuesdayfrom_hour').val())
            formData.append('tuesdayto_hour', $('#tuesdayto_hour').val())
            formData.append('wednesdayfrom_hour', $('#wednesdayfrom_hour').val())
            formData.append('wednesdayto_hour', $('#wednesdayto_hour').val())
            formData.append('thrusdayfrom_hour', $('#thrusdayfrom_hour').val())
            formData.append('thrusdayto_hour', $('#thrusdayto_hour').val())
            formData.append('fridayfrom_hour', $('#fridayfrom_hour').val())
            formData.append('fridayto_hour', $('#fridayto_hour').val())
            formData.append('saturdayfrom_hour', $('#saturdayfrom_hour').val())
            formData.append('saturdayto_hour', $('#saturdayto_hour').val())

            for (var i = 0; i < files_photo.length; i++) {
                formData.append('images' + i, files_photo[i])
            }
            formData.append('csrfmiddlewaretoken', '{{ csrf_token }}')

            $.ajax({
                type: 'POST',
                url: '{% url "create_store" %}',
                data: formData,
                cache: false,
                processData: false,
                contentType: false,
                enctype: 'multipart/form-data',
                success: function (){
                   window.location.replace("/");
                },
                error: function(xhr, errmsg, err) {
                    console.log(xhr.status + ":" + xhr.responseText);
                    alert("Please fill all details");
                }
            })
        })
    })