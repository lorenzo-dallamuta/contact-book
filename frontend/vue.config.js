const { SourceMapConsumer, SourceMapGenerator } = require('source-map')

// You should place this declaration somewhere at the top of your file
const sourceMaps = {}

module.exports = {
    configureWebpack: {
        devtool: 'source-map',
        plugins: [
            {
                apply(compiler) {
                    compiler.hooks.thisCompilation.tap(
                        'Initializing Compilation',
                        (compilation) => {
                            compilation.hooks.succeedModule.tap(
                                'Module Built',
                                (module) => {
                                    const { resource } = module

                                    // If "resource" is not set, ignore this module
                                    if (!resource) return

                                    // Ignore all modules that originated from the "node_modules" directory
                                    if (/node_modules/.test(resource)) return

                                    // Ignore all non-Single File Component files
                                    if (!/\.vue/.test(resource)) return

                                    // If this module is not of the template type, we should ignore it
                                    if (!/type=template/.test(resource)) return

                                    // Each module's source map will be held in "module._source._sourceMap", so
                                    // if this module does not contain a source map, we should ignore it
                                    if (
                                        !module['_source'] ||
                                        !module['_source']['_sourceMap']
                                    )
                                        return

                                    // If we've come this far, this is a module that we are interested in.

                                    // Store the module’s source map under its absolute path.  Note, however, that
                                    // we want to remove the query (e.g. “?vue&type=template&id=7ba5bd90”) from the
                                    // path before storing it
                                    const pathWithoutQuery =
                                        module.resource.replace(/\?.*$/, '')

                                    sourceMaps[pathWithoutQuery] =
                                        module['_source']['_sourceMap']
                                }
                            )
                            compilation.hooks.finishModules.tapPromise(
                                'All Modules Built',
                                async (modules) => {
                                    for (const module of modules) {
                                        const { resource } = module

                                        if (!resource) continue
                                        if (/node_modules/.test(resource))
                                            continue
                                        if (!/\.vue/.test(resource)) continue

                                        // Notice that we are targeting the modules with the "script" type now
                                        if (!/type=script/.test(resource))
                                            continue

                                        // Remember that we want to leave JavaScript Single File Components alone
                                        if (!/lang=ts/.test(resource)) continue
                                        if (
                                            !module['_source'] ||
                                            !module['_source']['_sourceMap']
                                        )
                                            continue

                                        // Again, if we make it this far, this is a module we’re interested in

                                        const pathWithoutQuery =
                                            module.resource.replace(/\?.*$/, '')
                                        const templateSourceMap =
                                            sourceMaps[pathWithoutQuery]

                                        // Skip this module if it doesn't have a corresponding template Source Map
                                        if (!templateSourceMap) continue

                                        // Store the source map for the current module
                                        const scriptSourceMap =
                                            module['_source']['_sourceMap']
                                        scriptSourceMap.sources = [
                                            ...templateSourceMap.sources,
                                        ]
                                        scriptSourceMap.sourcesContent = [
                                            ...templateSourceMap.sourcesContent,
                                        ]

                                        // This regular expression will split the source content into an array,
                                        // where each index holds a single line of the source content
                                        const lines = (
                                            templateSourceMap
                                                .sourcesContent[0] || ''
                                        ).match(/.+/g)

                                        let indexOfScriptTag = 0

                                        for (const line of lines) {
                                            ++indexOfScriptTag
                                            // Test the line to see if it has the opening tag
                                            if (/<script/.test(line)) break
                                        }

                                        // This function will create a consumer based on the script’s source map
                                        const shiftedSourceMap =
                                            await SourceMapConsumer.with(
                                                scriptSourceMap,
                                                null,
                                                async (consumer) => {
                                                    // This generator will create and hold the offset mappings
                                                    const generator =
                                                        new SourceMapGenerator()

                                                    // The consumer has the capability to iterate through each individual mapping
                                                    consumer.eachMapping(
                                                        (mapping) => {
                                                            // The “generatedLine” and “generatedColumn” variables refer to a position
                                                            // in the generated (i.e. built) file whereas the “originalLine” and
                                                            // “originalColumn” variables refer to the position of where the given
                                                            // line/column of code came from in the original source file
                                                            const {
                                                                generatedColumn,
                                                                generatedLine,
                                                                originalColumn,
                                                                originalLine,
                                                            } = mapping

                                                            let name =
                                                                mapping.name

                                                            // Notice that we are pulling down the source from the template Source Map
                                                            let source =
                                                                templateSourceMap
                                                                    .sources[0] ||
                                                                null

                                                            // Some mappings won’t have an original position. If this is the case
                                                            // we must make sure to null out the “name” and the “source” attributes
                                                            // otherwise the generator will throw an error
                                                            if (
                                                                originalLine ===
                                                                    null ||
                                                                originalColumn ===
                                                                    null
                                                            ) {
                                                                name = null
                                                                source = null
                                                            } else {
                                                                original = {
                                                                    column: originalColumn,
                                                                    line:
                                                                        originalLine +
                                                                        indexOfScriptTag,
                                                                }
                                                            }

                                                            // I found it odd that the generator expects the mappings to be in
                                                            // a format that is different to what the consumer provides them as
                                                            generator.addMapping(
                                                                {
                                                                    generated: {
                                                                        column: generatedColumn,
                                                                        line: generatedLine,
                                                                    },
                                                                    original,
                                                                    source,
                                                                    name,
                                                                }
                                                            )
                                                        }
                                                    )

                                                    // Once all of the mappings have been shifted and added, we need to
                                                    // convert the newly created Source Map to JSON and return it
                                                    return generator.toJSON()
                                                }
                                            )
                                        scriptSourceMap.mappings =
                                            shiftedSourceMap.mappings
                                    }
                                }
                            )
                        }
                    )
                },
            },
        ],
    },
}
