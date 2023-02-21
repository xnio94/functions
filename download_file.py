def download_file(request):
    return "done"
#
#
# def downloadFile(request):
#     action = request.args.get('action')
#     if action == 'download_clips':
#         episo de_link = request.args.get('episode_link')
#         count = request.args.get('count')
#         count = int(count)
#         title, urls = get_title_urls(episode_link)
#         # urls = urls[0:count]
#         if count == -1:
#             count = len(urls) - 1
#
#         valid_count = 0
#         for i in range(count):
#             filename = os.path.join('./', str(valid_count) + ".mp4")
#             if os.path.exists(filename):
#                 os.remove(filename)
#             try:
#                 urllib.request.urlretrieve(urls[i], filename)
#                 valid_count = valid_count + 1
#             except:
#                 print("An exception occurred")
#
#         with open("list.txt", "w") as f:
#             for i in range(valid_count):
#                 f.write(f"file {i}.mp4\n")
#
#         return jsonify({"title": title})
#
#     if action == 'merge':
#         title = request.args.get('title')
#         if os.path.exists(title):
#             os.remove(title)
#         command = "ffmpeg -f concat -i list.txt -c copy " + title
#         x = subprocess.run(command, shell=True)
#         return jsonify({"ready": "Ok"})
#
#     if action == 'download':
#         title = request.args.get('title')
#         return send_file(title, as_attachment=True)
