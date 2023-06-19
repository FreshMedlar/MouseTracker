# On normalization of the samples in the mouse movement
Normalizing each sample individually is likely better than normalizing all samples together in this case. Here's why:

    The samples represent different paths to reach a point. Each path likely has a different range of coordinates.

    Normalizing all samples together would force all paths to have the same normalized range, which may not be ideal.

    Normalizing each sample individually allows it to have its own appropriate normalized range, based on the actual coordinate values in that path.

    This helps preserve the relative differences between coordinates within each path, which is important information for the RNN to learn.

    Normalizing all samples together could squash or stretch the relative differences between coordinates within each path.

So in summary, I would recommend:

    Loop through each sample (path) individually
    Calculate the mean and standard deviation of the x and y coordinates for that sample
    Normalize the x and y coordinates for that sample using its own mean and std
    Store the normalized sample
    Repeat for all samples

This will:

    Allow each sample to have its own appropriate normalized range
    Preserve the relative coordinate differences within each sample
    Which is important information for the RNN to learn

On the other hand, normalizing all samples together could:

    Force all samples to have the same normalized range
    Potentially squash or stretch the relative coordinate differences within each sample

Hope this helps explain why normalizing each sample individually is likely better for your use case! Let me know if you have any other questions.